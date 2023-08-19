<svelte:head>
<title>Ionic Companion - Debug</title>
<meta name="Test Mode" content="Test" />
</svelte:head>

<script lang="ts">
import arrow_back from "$lib/images/arrow-back-outline.svg"
import arrow_forward from "$lib/images/arrow-forward-outline.svg"
import arrow_down from "$lib/images/arrow-down-outline.svg"
import arrow_up from "$lib/images/arrow-up-outline.svg"
import buddy_svg from "$lib/images/faces/buddy_svg.svg"

</script>

<ion-content fullscreen class="ion-padding">
	<ion-header translucent={true}>
	  <ion-toolbar>
		<ion-buttons slot="start">
		  <ion-menu-button />
		</ion-buttons>
		<ion-buttons slot="end">
		</ion-buttons>
			<ion-title>Debug</ion-title>
	 </ion-toolbar>
	 </ion-header>
	<ion-card>
		<ion-card-header>
		<!--<ion-card-subtitle>Check configuration</ion-card-subtitle>-->
		<!--<ion-card-title>DEBUG MODE</ion-card-title>-->
	</ion-card-header>

	<ion-card-content>
		<!--Vous pouvez écrire votre message ici-->
	</ion-card-content>
	<ion-item>
		<ion-button aria-label="Favorite">
			<ion-icon icon={arrow_up}></ion-icon>
		  </ion-button>
	</ion-item>
	<ion-item>
		<ion-button aria-label="Favorite">
			<ion-icon icon={arrow_back}></ion-icon>
		  </ion-button>

		<ion-button aria-label="Favorite">
			<ion-icon icon={arrow_forward}></ion-icon>
		  </ion-button>
	</ion-item>
	<ion-item>
		<ion-button aria-label="Favorite">
			<ion-icon icon={arrow_down}></ion-icon>
		  </ion-button>
	</ion-item>
	<ion-item>
		<ion-button aria-label="Favorite" fill="clear" color="dark" slot="end">Buddy SVG
			<ion-icon slot="icon-only" size="large"icon={buddy_svg}></ion-icon>
		  </ion-button>
	</ion-item>

</ion-card>

</ion-content>
