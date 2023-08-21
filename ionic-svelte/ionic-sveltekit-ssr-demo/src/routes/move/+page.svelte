<svelte:head>
<title>Ionic Companion - Debug</title>
<meta name="Action" content="Robot move" />
</svelte:head>

<script lang="ts">
import arrow_back from "$lib/images/arrow-back-outline.svg"
import arrow_forward from "$lib/images/arrow-forward-outline.svg"
import arrow_down from "$lib/images/arrow-down-outline.svg"
import arrow_up from "$lib/images/arrow-up-outline.svg"

</script>

<ion-content fullscreen class="ion-padding">
	<ion-header translucent={true}>
	  <ion-toolbar>
		<ion-buttons slot="start">
		  <ion-menu-button />
		</ion-buttons>
		<ion-buttons slot="end">
		</ion-buttons>
			<ion-title>Move</ion-title>
	 </ion-toolbar>
	 </ion-header>
	<ion-card>
		<ion-card-header>
		<!--<ion-card-subtitle>Check configuration</ion-card-subtitle>-->
		<!--<ion-card-title>MOVE MODE</ion-card-title>-->
	</ion-card-header>

	<ion-card-content>
		<!--Vous pouvez écrire votre message ici-->
	</ion-card-content>
	<ion-item>
		<div class="keypad">
			<ion-button disabled fill="clear" />
			  <ion-button aria-label="Favorite" color="dark">
				<ion-icon size="large"icon={arrow_up}></ion-icon>
			  </ion-button>
			  <ion-button disabled fill="clear" />
			  <ion-button aria-label="Favorite" color="dark">
				<ion-icon size="large"icon={arrow_back}></ion-icon>
			  </ion-button>
			  <ion-button disabled fill="outline" shape="round" color="dark" strong>MOVE</ion-button>
			  <ion-button aria-label="Favorite" color="dark">
				<ion-icon size="large"icon={arrow_forward}></ion-icon>
			  </ion-button>
			  <ion-button disabled fill="clear" />
			  <ion-button aria-label="Favorite" color="dark">
				<ion-icon size="large"icon={arrow_down}></ion-icon>
			  </ion-button>
			  <ion-button disabled fill="clear" />
		</div>
	</ion-item>

</ion-card>

</ion-content>

<style>
	.keypad {
		display: grid;
		grid-template-columns: repeat(3, 4em);
		grid-template-rows: repeat(3, 4em);
		grid-gap: 0.5em;
	}
</style>