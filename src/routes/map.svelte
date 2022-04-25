<script>
	import { onMount } from 'svelte';
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

	onMount(async () => {
		const L = await import('leaflet');

		map = L.map('map').setView([43.67, 7.21], 13);
		L.tileLayer('https://a.tile.openstreetmap.org/{z}/{x}/{y}.png ', {
			attribution:
				'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
			maxZoom: 18
		}).addTo(map);

		const stations = await getStations().then((match) => json5.parse(match));

		stations.forEach((station) => {
			const marker = L.marker(station['latlng']).addTo(map);
			marker.bindTooltip(`Free bikes: ${station['ab']}<br>Free slots: ${station['ap']}`);
			if (station['ab'] == 0) {
				marker._icon.classList.add('redmarker');
			}
			if (station['ap'] == 0) {
				marker._icon.classList.add('pinkmarker');
			}
		});
	});
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
		crossorigin="">
	</script>

	<script src="https://unpkg.com/json5@^2.0.0/dist/index.min.js"></script>
</svelte:head>

<div id="map" />

<style>
	#map {
		height: 90vh;
	}
</style>
