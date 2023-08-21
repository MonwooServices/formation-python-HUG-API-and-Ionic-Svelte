<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	export let value = '';

	const dispatch = createEventDispatcher();

	const select = (num:any) => () => (value += num);
	const clear = () => (value = '');
	const submit = () => dispatch('submit');
	import buddy_svg from "$lib/images/arrow-up-outline.svg"
</script>

<div class="keypad">
	<ion-button disabled fill="clear" />
	  <ion-button aria-label="Favorite" color="dark">
		<ion-icon size="large"icon={buddy_svg}></ion-icon>
	  </ion-button>
	  <ion-button disabled fill="clear" />
	  <ion-button aria-label="Favorite" color="dark">
		<ion-icon size="large"icon={buddy_svg}></ion-icon>
	  </ion-button>
	  <ion-button disabled fill="outline" shape="round" color="dark" strong>MOVE</ion-button>
	  <ion-button aria-label="Favorite" color="dark">
		<ion-icon size="large"icon={buddy_svg}></ion-icon>
	  </ion-button>
	  <ion-button disabled fill="clear" />
	  <ion-button aria-label="Favorite" color="dark">
		<ion-icon size="large"icon={buddy_svg}></ion-icon>
	  </ion-button>
	  <ion-button disabled fill="clear" />
</div>

<style>
	.keypad {
		display: grid;
		grid-template-columns: repeat(3, 4em);
		grid-template-rows: repeat(3, 4em);
		grid-gap: 0.5em;
	}
</style>