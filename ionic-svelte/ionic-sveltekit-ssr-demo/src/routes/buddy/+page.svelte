<script lang="ts">
import buddy from '$lib/images/Buddy_Transparent_01.webp';
import buddy_fallback from '$lib/images/Buddy_Transparent_01.png';
import { IonNav } from 'ionic-svelte';
import NavHome from '$lib/components/NavHome.svelte';
import { loadingController } from 'ionic-svelte';
import { IonPage } from 'ionic-svelte';
import SourceButton from '$lib/components/SourceButton.svelte';
import { toastController } from 'ionic-svelte';

const showToast = async () => {
	const toast = await toastController.create({
		color: 'danger',
		duration: 4000,
		message: 'This is a test !!!'
		});
	toast.present();
	};

	const showLoading = async () => {
		const options = {
		message: 'Loading......',
		duration: 30000
		};
		const loading = await loadingController.create(options);
		loading.present();
		setTimeout(() => {
			loading.dismiss();
			}, 2000);
		showToast();
		};

</script>

<svelte:head>
<title>Ionic Companion - Loading</title>
</svelte:head>

<IonPage>
		<ion-content fullscreen class="ion-padding">
		   <!-- svelte-ignore a11y-click-events-have-key-events -->
		   <!-- svelte-ignore a11y-no-static-element-interactions -->
		   <ion-button on:click={showLoading}>Click me!</ion-button>
		</ion-content>
		<ion-card>
			<img src={buddy} alt="buddy" />
			<ion-card-header>
				<ion-card-subtitle>SOLUTIONS ROBOTIQUES ÉMOTIONNELLES DÉDIÉES</ion-card-subtitle> 
				<ion-card-title>BUDDY, LE ROBOT EMOTIONNEL</ion-card-title>
			</ion-card-header>
			<ion-card-content>
				BUDDY peut améliorer la vie de tous,
				et plus particulièrement créer des liens sociaux,
				soutenir l'apprentissage des enfants,
				veiller et prendre soin de nos aînés.
			</ion-card-content>
		</ion-card>
		<ion-router-link href="/navigation#/page-one">
			<ion-button>Next Page</ion-button>
		</ion-router-link>
</IonPage>