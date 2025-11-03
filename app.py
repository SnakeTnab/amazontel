import streamlit as st
import requests
import json
from datetime import datetime
import urllib.parse


@st.cache_data
def search_amazon_data(scannable_id, local_date, route_number):
    cookies = {
        'ubid-acbfr': '260-2943062-6095419',
        'x-amz-log-portal-locale': 'fr-FR',
        'cwr_u': '79b61410-1164-4dcd-8580-d6e68bf2599f',
        'i18n-prefs': 'EUR',
        'lc-acbfr': 'fr_FR',
        'sst-acbfr': 'Sst1|PQF1VaWX0byHK9S87JS5GeQyCa2bhRZJYQ5_vtZOyCFiyDvDissy3urTxw-h71RGk-CLj4Lj13gAZ9LsO_0AEI38Cvnt_sKzw6kXCg7kOwOm007iDQ7dwA0fVrT6k0joN8zQXjR-aZQ5UssZw_6TX4GfYGm7Jq-k3tPF1e_cTeWPud-UFhoAUvA-Baj_SbF5qmutlA-owoOQdujV3qr5qDQy2j6pa-T2pUVZeuV9QnifuXbolstuurfauHylo8FkAoMfZAs2Y9G_ACu9gfnZah6CVjT2AWZvpwhmu9iUBPVtPRM',
        'at-acbfr': 'Atza|gQAEwzicAwEBAi569yN405_IxxtQqCGuyy90fAT6ItyvsMglIW1qPzph4GsuCWbvuyznTWpy572BB3b7cQ-PCGiHsLI9KAINl1yHJ7BUPey8_RBz5gGUffmdNPi8N6_VkBpIv8FlJW549hZYQIMmw3GC2fjxLN-wHt_u-66FP5vMXRTnYhMknEq_g4ALBQOXV4czYRHN9XYtDYjrL7VuIGjTg36sZi6tkU_chk3puv2PR4Qt6jmppJsycsyq7UtjaUCm9g0j5zr5nqGaN4QBCEGIkuHnvWWOB7SKegmPbEvYDFgyXrvcYTGzfYScVpWXbThFpsOj9HMzrTMQHIROJ9DW',
        'sess-at-acbfr': '"dVT/IQwLpP71XgUXLKqjjxxL9ZifNKefhZ0jVf6DSyk="',
        'session-id-time': '2082787201l',
        'ak_bmsc': 'D623F4A85EC015D972E1A0D542F4DF7D~000000000000000000000000000000~YAAQxNhLF6pYWiiaAQAAj6hfSR18sZg0Rl3ygpT25sv3zefSKPq39WpdarseFUaNKHuLftOkHf51HDFBIbCPuy+pNGCF6WKuIYVXJHTdjPNy1pOHSNGgGulBzqODoosbufPczIn0M45dToOKjr6qoEZMVTFPFvGHHZl7otH8+XAwPfb/lxAv4k8rBR2C3+ywPZsHOli90f7wZ9+snaTSU/YslPpm2RIyB1bqSzzzrIhGxOC7X3mZdlCBSs1lTcW5Y32S2vR9B8RgOQrLBl3eu1RlvBmtscd5LMP7x6iW2eZcE9bCj9A1iVHgvPNL28G2lM3e2/v0SEqdEjESpHXYQIWijlKaE/dHvcn+oygFXFAb8NnW5bh0P60EELTsu2x4QGhCvllBh0NlEzs=',
        'bm_sv': '170A1ABD8F1BBB79A658ED9CF6719FCB~YAAQxNhLF6WKWiiaAQAAO4ZgSR2UWbswpLk2dwsyfE0BXpBOvir7mwSnPlyjDn3vYlTfqNLd6q0aCBGauKMFrUDknUlq7JpZgrZkiff2t3aCD5fu6BKuuaPmiHnFFHtDhyj5kjJAFrAGj5ZASbl7cB7PZhl7RcMmN771X/EPZScmgCITr+p3lSZwwWDlAR9jvK7WBp903aijpkDJ+4VmG8zD5WZvBEVYwTRXW5LDqLcFvSx0sVXkVc7Bz39n3nk=~1',
        'session-id': '262-3184298-6525947',
        'x-acbfr': 'e8O9jKs94yqUjgdJByW5EWuWDMzPbEge5vgG?4CCNFLPCWPrjtMT2?hGcD0VsLV3',
        'session-token': 'SvcEA/S6SOT93pKjKSnqNmSP7dGDzDyRR5tlfaEJqcgvAOpq03p3zSt//eBVpRQV+Vc6vYy368wVUJ88YxeXvkZeVQWIsBw3v0svuXPZyJxGGnm+uT0IPpiVXGjeCYOGhP7mzTc6GQWsxERkwk274/c4q2N07EcDoIY+fykFgxIHxrq0aoKR+brvAtEFktwU1JVafrQvb6b5kKIM+mHOoTkE87sBFaReBx6aqnO4MaD5ixXQKOAuUbliyx7Kzwstdn08WwI4quZlZo6CdqDWnwC+0etic9mK741ebUb8MoYt5+X7ST3Uwo75gpWQbmicyyQq67MypzQP0ToW44CbSdEe/AvWpz3rAARfrm1lar5b8lucV78K73t13zkJog78',
        'cwr_s': 'eyJzZXNzaW9uSWQiOiJiN2UwNTM1My1lYzUxLTRhYTYtYTAyMy00ZjVlMTIxMmViNTQiLCJyZWNvcmQiOnRydWUsImV2ZW50Q291bnQiOjYzNywicGFnZSI6eyJwYWdlSWQiOiIvb3BlcmF0aW9ucy9leGVjdXRpb24vZHYvcm91dGVzIiwicGFyZW50UGFnZUlkIjoiL29wZXJhdGlvbnMvZXhlY3V0aW9uLyIsImludGVyYWN0aW9uIjoxNzMsInJlZmVycmVyIjoiaHR0cHM6Ly9sb2dpc3RpY3MuYW1hem9uLmZyL29wZXJhdGlvbnMvZXhlY3V0aW9uL2R2L3JvdXRlcy83MTUzNjUxLTI1Nz9uYXZNZW51VmFyaWFudD1leHRlcm5hbCZwcm92aWRlcj1BTExfRFJJVkVSUyZzZWxlY3RlZERheT0yMDI1LTExLTAzJnNlcnZpY2VBcmVhSWQ9ZDQ1OTc4OGItNmE3My00OGY5LWE3MTMtODFhZmEwYzU5YjY2JnRyYW5zcG9ydGVyPUFWM04yVlZGUzFXOTIiLCJyZWZlcnJlckRvbWFpbiI6ImxvZ2lzdGljcy5hbWF6b24uZnIiLCJzdGFydCI6MTc2MjE3MDYzNjM4MX19',
    }

    params = {
        'historicalDay': 'false',
        'localDate': local_date,
        'serviceAreaId': 'd459788b-6a73-48f9-a713-81afa0c59b66',
        'statsFromSummaries': 'true',
    }

    response = requests.get('https://logistics.amazon.fr/operations/execution/api/route-summaries', params=params, cookies=cookies)

    if response.status_code == 200:
        data = json.loads(response.text)
        all_route_ids = []

        for itinerary in data['itinerarySummaries']:
            route_ids = [route['routeId'] for route in itinerary['routes']]
            all_route_ids.extend(route_ids)

        prefixed_route_ids = [f"https://logistics.amazon.fr/operations/execution/api/routes/{route_id}" for route_id in all_route_ids]

        if route_number.isdigit():
            route_number = int(route_number)
            matching_route_links = []

            for route_link in prefixed_route_ids:
                parts = route_link.split('/')
                last_part = parts[-1]
                route_id = last_part.split('-')[-1]

                if route_id.isdigit() and int(route_id) == route_number:
                    matching_route_links.append(route_link)

            if matching_route_links:
                for route_link in matching_route_links:
                    route_response = requests.get(route_link, cookies=cookies)

                    if route_response.status_code == 200:
                        route_data = json.loads(route_response.text)
                    else:
                        st.error(f"Échec de la récupération des données pour l'URL {route_link} avec le code d'état : {route_response.status_code}")
            else:
                st.warning(f"Aucune URL correspondante trouvée pour le numéro de route {route_number}.")
        else:
            st.warning("Le numéro de route doit être un entier.")
    else:
        st.error("Échec de la récupération des données logistiques Amazon.")

    infos = get_info_by_scannable_id(route_data, scannable_id)
    return infos

def get_info_by_scannable_id(route_data, scannable_id):
    matching_infos = []

    for stop in route_data['routePlan']['stopList']:
        for package in stop['stopDetails']['packageList']:
            if package['scannableId'] == scannable_id:
                address_info = stop['stopDetails']['address']
                matching_infos.append({
                    'name': address_info['name'],
                    'address1': address_info['address1'],
                    'address2': address_info.get('address2', ''),
                    'postalCode': address_info['postalCode'],
                    'city': address_info['city'],
                    'phone': address_info.get('phone', '')
                })

    matching_infos = matching_infos[1:]
    return matching_infos
    
def share_on_whatsapp(result):
    message = f"Nom: {result['name']}\nAdresse 1: {result['address1']}\nAdresse 2: {result['address2']}\nCode postal: {result['postalCode']}\nVille: {result['city']}\nTéléphone: {result['phone']}"
    
    # Créez un lien WhatsApp avec le message pré-rempli
    whatsapp_link = f"https://wa.me/?text={urllib.parse.quote_plus(message)}"
    print("WhatsApp Link:", whatsapp_link)  # Ajoutez cette ligne
    
    # Affichez le lien généré
    st.success("Lien WhatsApp généré:")
    st.markdown(f"[Partager sur WhatsApp]({whatsapp_link})", unsafe_allow_html=True)
    
def main():
    # Définir l'icône de la page avec un emoji téléphone
    st.set_page_config(page_icon="📞", page_title="Amazon Client")

    st.title("Amazon Client")

    local_date = st.date_input("Date :", min_value=datetime(2022, 1, 1), max_value=datetime(2200, 1, 1))
    route_number = st.text_input("Numéro de route :")
    scannable_id = st.text_input("Numéro de colis :")

    if st.button("Rechercher"):
        # Convertir scannable_id en majuscules
        scannable_id = scannable_id.upper()
        formatted_date = local_date.strftime("%Y-%m-%d")
        results = search_amazon_data(scannable_id, formatted_date, route_number)
        
        if not results:
            st.warning("Aucun résultat trouvé.")
        else:
            for result in results:
                st.write("Nom :", result['name'])
                st.write("Adresse 1 :", result['address1'])
                st.write("Adresse 2 :", result['address2'])
                st.write("Code postal :", result['postalCode'])
                st.write("Ville :", result['city'])
                st.write("Téléphone :", result['phone'])
                st.write("-" * 30)
                
             # Ajoutez un bouton pour partager sur WhatsApp
            if st.button("Partager sur WhatsApp"):
                    share_on_whatsapp(result)

# Ajout du pied de page
    st.markdown(
        """
        <div style="text-align:center; margin-top: 30px; color: #888;">
            <hr>
            <p>© 2024 Big BoSs. Tous droits réservés.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
if __name__ == "__main__":
    main()
