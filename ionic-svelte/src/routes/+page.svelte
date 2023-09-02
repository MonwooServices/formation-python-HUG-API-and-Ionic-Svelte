<svelte:head>
	<title>Ionic Companion - Presentation</title>
	<meta name="Buddy" content="The emotional robot" />
</svelte:head>
	
<script lang="ts">
	import buddy from '$lib/images/Buddy_Transparent_01.webp';
	import { dev } from '$app/environment';
	import {onMount} from 'svelte';

	onMount(function(){
		if (dev) {
			//do in dev mode
			console.log("mode_dev")
		}
	})
</script> 

<ion-content fullscreen class="ion-padding">
	<ion-header translucent={true}>
	  <ion-toolbar>
		<ion-buttons slot="start">
		  <ion-menu-button />
		</ion-buttons>
		<ion-buttons slot="end">
		</ion-buttons>
			<ion-title>Home</ion-title>
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
		<img src={buddy} alt="buddy" />
	</ion-card>
	<div class="text-column">
		<p>
			BUDDY, le robot émotionnel, peut améliorer la vie de tous, et plus particulièrement,
			créer des liens sociaux, soutenir l'apprentissage des enfants, veiller et prendre soin de nos aînés.
		</p>
	
		<p>
			Un partenaire à la personnalité attachante au service du bien vieillir de nos aînés vivant seuls à la maison ou en institution,
			pour veiller sur eux, animer leur quotidien et les sortir de leur isolement.
		</p>
	
		<p>
			Un outil pédagogique pour permettre aux élèves d'apprendre différemment tout en s'amusant et de les préparer simplement au monde de demain:
			Partenaire d'apprentissage, Autisme, Robot avatar de téléprésence.
		</p>
		
		<p>
			Le robot Buddy de Télépresence permet de lutter contre l'isolement des enfants empêchés,
			en longue convalescence, et les aide à matérialiser leur présence physique à distance,
			de manière unique, lorsqu’ils sont physiquement incapables d’aller à l’école.
		</p>
	
		<p>
			BUDDY est parfait pour enrichir votre expérience client, générer de l'intérêt et du trafic,
			présenter des offres et diriger en fonction des demandes, ainsi que pour vous divertir.
		</p>
	
		<p>
			Une plateforme ouverte et évolutive avec ses outils de développement (SDK)
			pour donner vie à un compagnon au potentiel incroyable.
			La seule limite d'utilisation est l'imagination !!!!
		</p>
	
	</div>
</ion-content>