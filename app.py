import streamlit as st
import requests
import json
from datetime import datetime
import urllib.parse

# -------------------- Fonctions --------------------

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
    'x-acbfr': 'HgK@ClXie7pnf1SftV?XFgyIUuDeY2yOZEmzHsyowLKseWBbIK0ysTNlA@oWcuzu',
    'session-token': 'RgjFprqU6KxEoqw0phN2HgNz6zMa/kKd3jK54oPSo7Gm+AiaURAEoDaN5Bx5H8aAGfzm8QOIBXOymOPjsfZk/A9Kq/AaA7P4zpSoaFI9V708/M411N3fHVczvofGYNLVV7nEUGtrgTWAhoFL9vUYBEcJW0QZX124Qmw1UgwLs7b9jE/EVCJqwr2XWp196TzRg0vioaVs1Y+7UlLAo7aJwhsbY5OxRBvom1XPbIULpUqYpHIFS2wv6JEBaPXRof6EOUtKlg3S9B6muU2Shh5P/2utl1HIJQHj41/EA/e7uJXc8jZp6bYxJ7EubWB9mikLoLKr4Ys/SkYyLZ/r1Zmx4tFzW6shhBeV7ZTHIh3HJirv6mm3vPX0m4Kvm0qJjDgv',
    'cwr_s': 'eyJzZXNzaW9uSWQiOiJiN2UwNTM1My1lYzUxLTRhYTYtYTAyMy00ZjVlMTIxMmViNTQiLCJyZWNvcmQiOnRydWUsImV2ZW50Q291bnQiOjgwMCwicGFnZSI6eyJwYWdlSWQiOiIvb3BlcmF0aW9ucy9leGVjdXRpb24vZHYvcm91dGVzIiwicGFyZW50UGFnZUlkIjoiL29wZXJhdGlvbnMvZXhlY3V0aW9uLyIsImludGVyYWN0aW9uIjoxNzYsInJlZmVycmVyIjoiaHR0cHM6Ly9sb2dpc3RpY3MuYW1hem9uLmZyL29wZXJhdGlvbnMvZXhlY3V0aW9uL2R2L3JvdXRlcz9uYXZNZW51VmFyaWFudD1leHRlcm5hbCZwcm92aWRlcj1BTExfRFJJVkVSUyZzZWxlY3RlZERheT0yMDI1LTExLTAzJnNlcnZpY2VBcmVhSWQ9ZDQ1OTc4OGItNmE3My00OGY5LWE3MTMtODFhZmEwYzU5YjY2IiwicmVmZXJyZXJEb21haW4iOiJsb2dpc3RpY3MuYW1hem9uLmZyIiwic3RhcnQiOjE3NjIxNzMzMjMwNjh9fQ==',
    }

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://logistics.amazon.fr/operations/execution/dv/routes?navMenuVariant=external&selectedDay=2025-11-03&serviceAreaId=d459788b-6a73-48f9-a713-81afa0c59b66',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'user-ref': 'cortex-webapp-user',
    'x-cortex-hmac-signature': 'B7kpFjwHLmVdQqNXzZrDiMU3/ku8Yiof8XNRMa1cKOs=',
    'x-cortex-session': '01334fe5f1a44e1a',
    'x-cortex-timestamp': '1762173323105',
    # 'cookie': 'ubid-acbfr=260-2943062-6095419; x-amz-log-portal-locale=fr-FR; cwr_u=79b61410-1164-4dcd-8580-d6e68bf2599f; i18n-prefs=EUR; lc-acbfr=fr_FR; sst-acbfr=Sst1|PQF1VaWX0byHK9S87JS5GeQyCa2bhRZJYQ5_vtZOyCFiyDvDissy3urTxw-h71RGk-CLj4Lj13gAZ9LsO_0AEI38Cvnt_sKzw6kXCg7kOwOm007iDQ7dwA0fVrT6k0joN8zQXjR-aZQ5UssZw_6TX4GfYGm7Jq-k3tPF1e_cTeWPud-UFhoAUvA-Baj_SbF5qmutlA-owoOQdujV3qr5qDQy2j6pa-T2pUVZeuV9QnifuXbolstuurfauHylo8FkAoMfZAs2Y9G_ACu9gfnZah6CVjT2AWZvpwhmu9iUBPVtPRM; at-acbfr=Atza|gQAEwzicAwEBAi569yN405_IxxtQqCGuyy90fAT6ItyvsMglIW1qPzph4GsuCWbvuyznTWpy572BB3b7cQ-PCGiHsLI9KAINl1yHJ7BUPey8_RBz5gGUffmdNPi8N6_VkBpIv8FlJW549hZYQIMmw3GC2fjxLN-wHt_u-66FP5vMXRTnYhMknEq_g4ALBQOXV4czYRHN9XYtDYjrL7VuIGjTg36sZi6tkU_chk3puv2PR4Qt6jmppJsycsyq7UtjaUCm9g0j5zr5nqGaN4QBCEGIkuHnvWWOB7SKegmPbEvYDFgyXrvcYTGzfYScVpWXbThFpsOj9HMzrTMQHIROJ9DW; sess-at-acbfr="dVT/IQwLpP71XgUXLKqjjxxL9ZifNKefhZ0jVf6DSyk="; session-id-time=2082787201l; ak_bmsc=D623F4A85EC015D972E1A0D542F4DF7D~000000000000000000000000000000~YAAQxNhLF6pYWiiaAQAAj6hfSR18sZg0Rl3ygpT25sv3zefSKPq39WpdarseFUaNKHuLftOkHf51HDFBIbCPuy+pNGCF6WKuIYVXJHTdjPNy1pOHSNGgGulBzqODoosbufPczIn0M45dToOKjr6qoEZMVTFPFvGHHZl7otH8+XAwPfb/lxAv4k8rBR2C3+ywPZsHOli90f7wZ9+snaTSU/YslPpm2RIyB1bqSzzzrIhGxOC7X3mZdlCBSs1lTcW5Y32S2vR9B8RgOQrLBl3eu1RlvBmtscd5LMP7x6iW2eZcE9bCj9A1iVHgvPNL28G2lM3e2/v0SEqdEjESpHXYQIWijlKaE/dHvcn+oygFXFAb8NnW5bh0P60EELTsu2x4QGhCvllBh0NlEzs=; bm_sv=170A1ABD8F1BBB79A658ED9CF6719FCB~YAAQxNhLF6WKWiiaAQAAO4ZgSR2UWbswpLk2dwsyfE0BXpBOvir7mwSnPlyjDn3vYlTfqNLd6q0aCBGauKMFrUDknUlq7JpZgrZkiff2t3aCD5fu6BKuuaPmiHnFFHtDhyj5kjJAFrAGj5ZASbl7cB7PZhl7RcMmN771X/EPZScmgCITr+p3lSZwwWDlAR9jvK7WBp903aijpkDJ+4VmG8zD5WZvBEVYwTRXW5LDqLcFvSx0sVXkVc7Bz39n3nk=~1; session-id=262-3184298-6525947; x-acbfr=HgK@ClXie7pnf1SftV?XFgyIUuDeY2yOZEmzHsyowLKseWBbIK0ysTNlA@oWcuzu; session-token=RgjFprqU6KxEoqw0phN2HgNz6zMa/kKd3jK54oPSo7Gm+AiaURAEoDaN5Bx5H8aAGfzm8QOIBXOymOPjsfZk/A9Kq/AaA7P4zpSoaFI9V708/M411N3fHVczvofGYNLVV7nEUGtrgTWAhoFL9vUYBEcJW0QZX124Qmw1UgwLs7b9jE/EVCJqwr2XWp196TzRg0vioaVs1Y+7UlLAo7aJwhsbY5OxRBvom1XPbIULpUqYpHIFS2wv6JEBaPXRof6EOUtKlg3S9B6muU2Shh5P/2utl1HIJQHj41/EA/e7uJXc8jZp6bYxJ7EubWB9mikLoLKr4Ys/SkYyLZ/r1Zmx4tFzW6shhBeV7ZTHIh3HJirv6mm3vPX0m4Kvm0qJjDgv; cwr_s=eyJzZXNzaW9uSWQiOiJiN2UwNTM1My1lYzUxLTRhYTYtYTAyMy00ZjVlMTIxMmViNTQiLCJyZWNvcmQiOnRydWUsImV2ZW50Q291bnQiOjgwMCwicGFnZSI6eyJwYWdlSWQiOiIvb3BlcmF0aW9ucy9leGVjdXRpb24vZHYvcm91dGVzIiwicGFyZW50UGFnZUlkIjoiL29wZXJhdGlvbnMvZXhlY3V0aW9uLyIsImludGVyYWN0aW9uIjoxNzYsInJlZmVycmVyIjoiaHR0cHM6Ly9sb2dpc3RpY3MuYW1hem9uLmZyL29wZXJhdGlvbnMvZXhlY3V0aW9uL2R2L3JvdXRlcz9uYXZNZW51VmFyaWFudD1leHRlcm5hbCZwcm92aWRlcj1BTExfRFJJVkVSUyZzZWxlY3RlZERheT0yMDI1LTExLTAzJnNlcnZpY2VBcmVhSWQ9ZDQ1OTc4OGItNmE3My00OGY5LWE3MTMtODFhZmEwYzU5YjY2IiwicmVmZXJyZXJEb21haW4iOiJsb2dpc3RpY3MuYW1hem9uLmZyIiwic3RhcnQiOjE3NjIxNzMzMjMwNjh9fQ==',
    }

    params = {
        'historicalDay': 'false',
        'localDate': local_date,
        'serviceAreaId': 'd459788b-6a73-48f9-a713-81afa0c59b66',
        'statsFromSummaries': 'true',
    }

    try:
        response = requests.get(
            'https://logistics.amazon.fr/operations/execution/api/route-summaries',
            params=params, cookies=cookies, headers=headers
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la récupération des routes : {e}")
        return []

    data = response.json()
    all_route_ids = [route['routeId'] for itinerary in data['rmsRouteSummaries'] for route in itinerary['routes']]
    prefixed_route_links = [f"https://logistics.amazon.fr/operations/execution/api/routes/{route_id}" for route_id in all_route_ids]

    route_data = None
    if route_number.isdigit():
        route_number = int(route_number)
        for route_link in prefixed_route_links:
            last_part = route_link.split('/')[-1]
            route_id = last_part.split('-')[-1]
            if route_id.isdigit() and int(route_id) == route_number:
                try:
                    route_response = requests.get(route_link, cookies=cookies, headers=headers)
                    route_response.raise_for_status()
                    route_data = route_response.json()
                    break
                except requests.exceptions.RequestException as e:
                    st.error(f"Erreur lors de la récupération de la route {route_number} : {e}")
    else:
        st.warning("Le numéro de route doit être un entier.")
        return []

    if not route_data:
        st.warning(f"Aucune donnée trouvée pour le numéro de route {route_number}.")
        return []

    return get_info_by_scannable_id(route_data, scannable_id)

def get_info_by_scannable_id(route_data, scannable_id):
    matching_infos = []

    for stop in route_data.get('routePlan', {}).get('stopList', []):
        for package in stop.get('stopDetails', {}).get('packageList', []):
            if package.get('scannableId') == scannable_id:
                address_info = stop['stopDetails'].get('address', {})
                matching_infos.append({
                    'name': address_info.get('name', ''),
                    'address1': address_info.get('address1', ''),
                    'address2': address_info.get('address2', ''),
                    'postalCode': address_info.get('postalCode', ''),
                    'city': address_info.get('city', ''),
                    'phone': address_info.get('phone', '')
                })
    return matching_infos

def generate_whatsapp_link(result):
    message = (
        f"Nom: {result['name']}\n"
        f"Adresse 1: {result['address1']}\n"
        f"Adresse 2: {result['address2']}\n"
        f"Code postal: {result['postalCode']}\n"
        f"Ville: {result['city']}\n"
        f"Téléphone: {result['phone']}"
    )
    return f"https://wa.me/?text={urllib.parse.quote_plus(message)}"

# -------------------- Interface Streamlit --------------------

def main():
    st.set_page_config(page_icon="📞", page_title="Amazon Client")
    st.title("Amazon Client")

    local_date = st.date_input(
        "Date :", min_value=datetime(2022, 1, 1), max_value=datetime(2200, 1, 1)
    )
    route_number = st.text_input("Numéro de route :")
    scannable_id = st.text_input("Numéro de colis :")

    if st.button("Rechercher"):
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
                
                whatsapp_link = generate_whatsapp_link(result)
                st.markdown(f"[Partager sur WhatsApp]({whatsapp_link})", unsafe_allow_html=True)
                st.write("---")

    # Pied de page
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
