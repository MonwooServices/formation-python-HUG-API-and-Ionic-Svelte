<script lang="ts">
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
      message: 'Here a random toast'
      // showCloseButton: true,
   });
   toast.present();
};

const showLoading = async () => {
   const options = {
      message: 'Please wait......',
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

<ion-app>
   <ion-nav root={NavHome}></ion-nav>
</ion-app>

<IonPage>
<ion-content fullscreen class="ion-padding">
   <!-- svelte-ignore a11y-click-events-have-key-events -->
   <!-- svelte-ignore a11y-no-static-element-interactions -->
   <ion-button on:click={showLoading}>Click me!</ion-button>
</ion-content>

</IonPage>
