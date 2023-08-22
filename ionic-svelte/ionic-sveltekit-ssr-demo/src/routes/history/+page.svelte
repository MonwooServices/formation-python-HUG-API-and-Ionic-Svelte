<svelte:head>
	<title>Ionic Companion - History</title>
	<meta name="History" content="Print history" />
</svelte:head>

<script lang="ts">
	import { onMount } from 'svelte';
	import { loadingController } from 'ionic-svelte';
	import { toastController } from 'ionic-svelte';
	let messageList:any = [];

async function showToast(color:any,message:any) {
	const toast = await toastController.create({
		color: color,
		duration: 4000,
		message: message
	});
	toast.present();
};

	async function showLoading() {
		const options = {
		message: 'Loading......',
		duration: 100
		};
		const loading = await loadingController.create(options);
		loading.present();
		setTimeout(() => {
		  loading.dismiss();
		  }, 2500
		);	
	};

	onMount(async function() {
		showLoading();	
		const queryString = window.location.search;
		const urlParams = new URLSearchParams(queryString);
		const backendIp = urlParams.get("backendIp") || "192.168.1.100";
		const backendPort = urlParams.get("backendPort") || "8000";
		await fetch(`http://${backendIp}:${backendPort}/api/buddy/read-msgs`).then(
        async resp => {
          const dataResp = await resp.json(); // this returns a promise
          const List = dataResp.buddy_messages
		  messageList = List.concat(List);
		  ////TIPS////
		  //messageList.forEach(function (value:any) {
  			//console.log(value);
		  //});
          return resp;
        }).then(repos => {
          console.log(repos)
        }).catch(ex => {
          console.error(ex);
		  showToast("danger","Echec");
        })
	});


</script>

<ion-content fullscreen class="ion-padding">
	<ion-header translucent={true}>
	  <ion-toolbar>
		<ion-buttons slot="start">
		  <ion-menu-button />
		</ion-buttons>
		<ion-buttons slot="end">
		</ion-buttons>
			<ion-title>History</ion-title>
	  </ion-toolbar>
	</ion-header>
	<ion-card>
		<ion-card-header>
		<!--<ion-card-subtitle>Check configuration</ion-card-subtitle>-->
		<!--<ion-card-title>HISTORY</ion-card-title>-->
		</ion-card-header>

	<ion-card-content>
		<!--Vous pouvez écrire votre message ici-->
	</ion-card-content>
	<ion-list>
		{#each messageList as message}
		<ion-item color="light">
		   <ion-label>{message}</ion-label>
		</ion-item>
		{/each}
	</ion-list>
	</ion-card>
	</ion-content>