<script>
	import * as JSON5 from 'json5';
	import { stations } from './store.js';
	import Map from './map.svelte';

	fetch('https://www.velobleu.org/en/nos-stations/')
		.then((response) => response.text())
		.then((text) => {
			const pattern = /var stations([^;]+)/g;
			const match = text
				.replace(/\n/g, '')
				.match(pattern)[0]
				.replace(/var stations = /g, '');
			$stations = JSON5.parse(match);
			console.log($stations);
		});
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<!-- {#each $stations as station}
    <p>{station["name"]}</p>
{/each} -->
<!-- <Map /> -->
