<script lang="ts">
import { onMount } from 'svelte';
import elvex from '$lib/images/Elvex_Domotique.png';
import { showMenu } from '$lib/services/menu';
import * as allIonicIcons from 'ionicons/icons';
import { goto } from '$app/navigation';
import { menuController, modalController, registerMenu } from 'ionic-svelte';
//import { dev } from '$app/environment';
const modules = import.meta.glob('../../**/*.svelte', { as: 'raw' });
let inlineModalOpen = false;
export let side: 'start' | 'end' | undefined = 'start';
$: hideMenu = !$showMenu;

onMount(() => {
		registerMenu('mainmenu');
	});

const closeAndNavigate = async (url: string) => {
		// take the google tag from the main thread
		setTimeout(() => {
			//@ts-ignore
			//if (!dev) window.gtag('event', url);
		}, 100);

		console.log('Navigate url', url);

		goto(url);
		menuController.close('mainmenu');
	};
let menuItems: Array<{ url: string; label: string; icon: any }> = Object.keys(modules)
		.filter((key) => key.includes('/routes/') && !key.includes('[tab]'))
		.map((key) =>
			capitalizeFirstLetter(
				key.replace('../../routes/', '').replace('/+page.svelte', '')
			)
		)
		.concat(['buddy'],['debug'],['face'],['history'],['message'],['move'],['test'])
		.sort()

		.map((componentName) => {
			console.log('COMPONENTN', componentName);
			const url =
				componentName !== 'Tabs' ? `${componentName}` : `/`;
			return {
				url,
				label: componentName,
				icon: allIonicIcons['home']
			};
		});

		const icons = Object.keys(allIonicIcons);
	menuItems.map((menuItem) => {
		const iconForMenu = icons[Math.floor(Math.random() * icons.length)];
		// @ts-ignore
		menuItem.icon = allIonicIcons[iconForMenu];
	});
	menuItems = [...menuItems];

		function capitalizeFirstLetter(text: string) {
		return text.charAt(0).toUpperCase() + text.slice(1);
		}
</script>

<ion-menu {side} content-id="main" menu-id="mainmenu" class:menuhide={hideMenu}>
	<ion-modal is-open={inlineModalOpen}>
		<br />

		<ion-content>
			<ion-card>
				<ion-card-header>
					<ion-card-title>Buddy - Le Robot émotionnel</ion-card-title>
				</ion-card-header>
				<ion-card-content>
					<p>Le programme a été développé sous Ionic-Svelte.</p>
					<br />
					<p>
						Il vous permettra d'intéragir facilement avec le robot.
					</p>
					<br />
					<p>
						Application proposée par ELVEX DOMOTIQUE
					</p>
					<br />
					<p>
						Vous pouvez visiter notre site internet:
					</p>
					<br />
					<p>
					<a
						href="https://elvex-domotique.fr"
						target="_new">https://elvex-domotique.fr</a>
					</p>
					<br /><br />
					<p>Amusez-vous bien ^^</p>
					<br />
					<img src={elvex} width="15%" alt="Feedback" />
				</ion-card-content>
			</ion-card>
			<br />
			<ion-button aria-hidden="true"
				expand="block"
				on:keyup={() => {
					inlineModalOpen = false;
				}}
				on:click={() => {
					inlineModalOpen = false;
				}}>
				Retour
			</ion-button>
		</ion-content>
	</ion-modal>



	{#if menuItems.length > 0}
		<ion-header>
			<ion-toolbar>
				<ion-title>Menu</ion-title>
				<ion-button aria-hidden="true"
					expand="block"
					on:keyup={() => {
						//@ts-ignore
						//window.gtag('event', 'Feedback open');
						inlineModalOpen = true;
					}}
					on:click={() => {
						//@ts-ignore
						//window.gtag('event', 'Feedback open');
						inlineModalOpen = true;
					}}
					slot="end">About...</ion-button>
			</ion-toolbar>
		</ion-header>
	<ion-content>
		<ion-list>
			{#each menuItems as menuItem, i}
				<ion-item aria-hidden="true"
					on:keyup={() => {
						closeAndNavigate(menuItem.url);
					}}
					on:click={() => {
						closeAndNavigate(menuItem.url);
					}}>
					<ion-icon icon={menuItem.icon} slot="start" color=black />
					<ion-label>{menuItem.label}</ion-label>
				</ion-item>
				{/each}
				<ion-item />
</ion-list>
</ion-content>
{/if}
</ion-menu>

<style>
	ion-item {
		cursor: pointer;
	}

	.menuhide {
		display: none;
	}
</style>