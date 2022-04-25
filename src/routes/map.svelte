<!-- <script>
    // https://svelte.dev/tutorial/context-api
	import * as L from 'leaflet';
	import { stations } from './store.js';
	let map;

	function createMap(container) {
		let m = L.map(container).setView([43.67, 7.21], 13);
		L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
			attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
            &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
			subdomains: 'abcd',
			maxZoom: 20
		}).addTo(m);

		let marker = L.marker([43.67, 7.21]).addTo(m);
		if ($stations.length > 0) {
			$stations.forEach((station) => {
				console.log(station.latlng);
				L.marker(station.latlng).addTo(m);
			});
		}

		return m;
	}

	function mapAction(container) {
		map = createMap(container);
		return {
			destroy: () => {
				map.remove();
			}
		};
	}
</script>

<svelte:head>
	<link
		rel="stylesheet"
		href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
		integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
		crossorigin=""
	/>
</svelte:head>

<div style="height:90vh;width:100%" use:mapAction /> -->
<script>
	import { onMount } from 'svelte';
	import { stations } from './store.js';
	import * as L from 'leaflet';

	let map;

	$: if ($stations.length == 0) {
		console.log(`no stations`);
		onMount(async () => {
			map = L.map('map').setView([43.67, 7.21], 13);
			L.tileLayer('https://a.tile.openstreetmap.org/{z}/{x}/{y}.png ', {
				attribution:
					'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
				maxZoom: 20
			}).addTo(map);

			L.marker([43.67, 7.21]).addTo(map);
		});
	} else {
		console.log('hm?');
	}

	$: {
		console.log($stations);
	}
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
</svelte:head>

<div id="map" />

<style>
	#map {
		height: 90vh;
	}
</style>
