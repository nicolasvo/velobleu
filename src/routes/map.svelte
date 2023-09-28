<script>
	import { onMount } from 'svelte';
	import { writable } from 'svelte/store';
	import json5 from 'json5';

	const getStations = async () => {
		const match = await fetch(
			`https://api.allorigins.win/get?url=${encodeURIComponent(
				'https://www.velobleu.org/en/nos-stations/'
			)}`
		)
			.then((response) => response.text())
			.then((text) => {
				const pattern = /var stations([^;]+)/g;
				const match = text
					.replace(/\\n/g, '')
					.replace(/\\/g, '')
					.match(pattern)[0]
					.replace(/var stations = /g, '');
				return match;
			});
		return match;
	};

	let map;

	map = onMount(async () => {
		const L = await import('leaflet');

		map = L.map('map').setView([43.67, 7.21], 13);
		// https://leaflet-extras.github.io/leaflet-providers/preview/

		L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
			attribution:
				'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
			subdomains: 'abcd',
			maxZoom: 20
		}).addTo(map);

		// L.tileLayer(
		// 	'https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
		// 	{
		// 		maxZoom: 20,
		// 		attribution:
		// 			'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012'
		// 	}
		// ).addTo(map);

		// L.tileLayer('https://tiles.stadiamaps.com/tiles/outdoors/{z}/{x}/{y}{r}.png', {
		// 	maxZoom: 20,
		// 	attribution:
		// 		'&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
		// }).addTo(map);

		const command = L.control({ position: 'bottomright' });
		command.onAdd = () => {
			const container = L.DomUtil.create('div', 'leaflet-bar leaflet-control');
			const button = L.DomUtil.create('a', 'leaflet-control-button', container);
			button.innerHTML =
				'<div class="flex justify-center items-center"><svg class="h-7" xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#000000"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M18.75 3.94L4.07 10.08c-.83.35-.81 1.53.02 1.85L9.43 14c.26.1.47.31.57.57l2.06 5.33c.32.84 1.51.86 1.86.03l6.15-14.67c.33-.83-.5-1.66-1.32-1.32z"/></svg></div>';
			L.DomEvent.disableClickPropagation(button);
			L.DomEvent.on(button, 'click', async () => {
				await getLocation();
			});

			container.title = 'Show user location';

			return container;
		};
		command.addTo(map);

		const stations = await getStations().then((match) => json5.parse(match));

		stations.forEach((station) => {
			const marker = L.marker(station['latlng']).addTo(map);
			marker.bindTooltip(`Bikes: ${station['ab']}<br>Slots: ${station['ap']}`);
			if (station['ab'] == 0) {
				marker._icon.classList.add('redmarker');
			}
			if (station['ap'] == 0) {
				marker._icon.classList.add('greenmarker');
			}
		});

		return map;
	});

	export const coordinates = writable();

	let userMarker;

	const getLocation = async () => {
		await navigator.geolocation.getCurrentPosition((position) => {
			const lat = position.coords.latitude;
			const lng = position.coords.longitude;
			$coordinates = [lat, lng];
			if (userMarker != undefined) {
				userMarker.removeFrom(map);
			}
			userMarker = L.marker($coordinates);
			userMarker.addTo(map);
			userMarker._icon.classList.add('pinkmarker');
			map.setView($coordinates, 16);
		});
	};
</script>

<svelte:head>
	<link
		rel="stylesheet"
		href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
		integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
		crossorigin=""
	/>

	<script
		src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"
		integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew=="
		crossorigin=""
	>
	</script>

	<script src="https://unpkg.com/json5@^2.0.0/dist/index.min.js"></script>
</svelte:head>

<div id="map" />

<style>
	#map {
		height: 100vh;
	}
</style>
