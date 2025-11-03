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
    'session-id': '262-3184298-6525947',
    'at-acbfr': 'Atza|gQBWgDB1AwEBAqg_27yBUxAz5qtNviHj1AKDnnyTVVwhYR654uJSvTFRceOZi-zGxAgvc48AkRWBBzvl-OW2XQVpU6wMJ-36voKGJrFdUrLhweDdMOv_mOS42YlKBwPqiIBDHLDwntmsQnyBCo4o54WHhKTQat6I56dHtuf7PX2Y1YKT7uigNYTuFweMAb2kFph9Anvmyj-IPbO6r2MjfOZ_r9R124lspOXxkbDpMP9ZOzcPrBZfkUc3QZqUagurTECA_RyaB-tNNXk0QjcY5TcVSkaMGeyGfeuBtlLhx-s0cjH_ikCJ7mEudcqMlKCG9b_H27n-Ed32PjI-dyzLw-Hr',
    'sess-at-acbfr': '"3TI7ZybCSHIeW2k8h5MG9WBcAqXeb7otlXqyAUYTCBo="',
    'session-id-time': '2082787201l',
    'cwr_s': 'eyJzZXNzaW9uSWQiOiJlN2Y3MGYwNS0zZjAxLTQ0M2UtYmNjYS0wOWZiZjhhZGY0YzEiLCJyZWNvcmQiOnRydWUsImV2ZW50Q291bnQiOjcwLCJwYWdlIjp7InBhZ2VJZCI6Ii9vcGVyYXRpb25zL2V4ZWN1dGlvbi9kdi9yb3V0ZXMiLCJwYXJlbnRQYWdlSWQiOiIvb3BlcmF0aW9ucy9leGVjdXRpb24vZHYvcm91dGVzLzcxNTM2NTEtMjU3IiwiaW50ZXJhY3Rpb24iOjE4MiwicmVmZXJyZXIiOiJodHRwczovL2xvZ2lzdGljcy5hbWF6b24uZnIvb3BlcmF0aW9ucy9leGVjdXRpb24vZHYvcm91dGVzLzcxNTM2NTEtMjU3P25hdk1lbnVWYXJpYW50PWV4dGVybmFsJnByb3ZpZGVyPUFMTF9EUklWRVJTJnNlbGVjdGVkRGF5PTIwMjUtMTEtMDMmc2VydmljZUFyZWFJZD1kNDU5Nzg4Yi02YTczLTQ4ZjktYTcxMy04MWFmYTBjNTliNjYmdHJhbnNwb3J0ZXI9QUxMX0RSSVZFUlMiLCJyZWZlcnJlckRvbWFpbiI6ImxvZ2lzdGljcy5hbWF6b24uZnIiLCJzdGFydCI6MTc2MjE4NjM5MDk4MX19',
    'x-acbfr': 'S6nVDF7DBQis7psHiQBPgmunzuEqBFBW8@wFhyUTnVbf5cMryEWf87QwajPPGFZC',
    'session-token': 'JnMCUjDnJVFwqeoHOtID5/Fa0ri1WAZcBIi5LjOenMmvPQOGWuaoDaeF/jpuYFVA2MYEBdY+jdwRSGT9+H4cszhjIrPISZ1PaKxHcgBTw0DuK/yYaf50cEjEKMJsd9XNiTwnb0C7wbL6frknvZRJsuo+O+UYrHWpd7AKkd8SyWdWya9AzLdXOgfumuGaLCTcP/mqNlSUuD+DnrpZkI++ZwRyUhLPPaxeO/TOodQBopEKjrQEKnn3DaTHN5aAVkbH1w1Jvo+o0FGtgAwThG4695QiWA1ItDeyKu/iJH0bJWbhKSf3Ela76RPwBfjp0I7I9mBkGgbrp9bi4CdYYz3iNfHzKlNQBqUssTKUkoOeZrx53Dqct3oZ4+xYRSUhoR4b',
    }

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://logistics.amazon.fr/operations/execution/dv/routes?navMenuVariant=external&provider=ALL_DRIVERS&selectedDay=2025-11-03&serviceAreaId=d459788b-6a73-48f9-a713-81afa0c59b66',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'user-ref': 'cortex-webapp-user',
    'x-cortex-hmac-signature': 'jS+zPy34Pr9gVe8x/tuvyEUhwgyuhQxzrccxUuJOPcA=',
    'x-cortex-session': '2230bdad96754e0a',
    'x-cortex-timestamp': '1762186565986',
    # 'cookie': 'ubid-acbfr=260-2943062-6095419; x-amz-log-portal-locale=fr-FR; cwr_u=79b61410-1164-4dcd-8580-d6e68bf2599f; i18n-prefs=EUR; lc-acbfr=fr_FR; sst-acbfr=Sst1|PQF1VaWX0byHK9S87JS5GeQyCa2bhRZJYQ5_vtZOyCFiyDvDissy3urTxw-h71RGk-CLj4Lj13gAZ9LsO_0AEI38Cvnt_sKzw6kXCg7kOwOm007iDQ7dwA0fVrT6k0joN8zQXjR-aZQ5UssZw_6TX4GfYGm7Jq-k3tPF1e_cTeWPud-UFhoAUvA-Baj_SbF5qmutlA-owoOQdujV3qr5qDQy2j6pa-T2pUVZeuV9QnifuXbolstuurfauHylo8FkAoMfZAs2Y9G_ACu9gfnZah6CVjT2AWZvpwhmu9iUBPVtPRM; session-id=262-3184298-6525947; at-acbfr=Atza|gQBWgDB1AwEBAqg_27yBUxAz5qtNviHj1AKDnnyTVVwhYR654uJSvTFRceOZi-zGxAgvc48AkRWBBzvl-OW2XQVpU6wMJ-36voKGJrFdUrLhweDdMOv_mOS42YlKBwPqiIBDHLDwntmsQnyBCo4o54WHhKTQat6I56dHtuf7PX2Y1YKT7uigNYTuFweMAb2kFph9Anvmyj-IPbO6r2MjfOZ_r9R124lspOXxkbDpMP9ZOzcPrBZfkUc3QZqUagurTECA_RyaB-tNNXk0QjcY5TcVSkaMGeyGfeuBtlLhx-s0cjH_ikCJ7mEudcqMlKCG9b_H27n-Ed32PjI-dyzLw-Hr; sess-at-acbfr="3TI7ZybCSHIeW2k8h5MG9WBcAqXeb7otlXqyAUYTCBo="; session-id-time=2082787201l; cwr_s=eyJzZXNzaW9uSWQiOiJlN2Y3MGYwNS0zZjAxLTQ0M2UtYmNjYS0wOWZiZjhhZGY0YzEiLCJyZWNvcmQiOnRydWUsImV2ZW50Q291bnQiOjcwLCJwYWdlIjp7InBhZ2VJZCI6Ii9vcGVyYXRpb25zL2V4ZWN1dGlvbi9kdi9yb3V0ZXMiLCJwYXJlbnRQYWdlSWQiOiIvb3BlcmF0aW9ucy9leGVjdXRpb24vZHYvcm91dGVzLzcxNTM2NTEtMjU3IiwiaW50ZXJhY3Rpb24iOjE4MiwicmVmZXJyZXIiOiJodHRwczovL2xvZ2lzdGljcy5hbWF6b24uZnIvb3BlcmF0aW9ucy9leGVjdXRpb24vZHYvcm91dGVzLzcxNTM2NTEtMjU3P25hdk1lbnVWYXJpYW50PWV4dGVybmFsJnByb3ZpZGVyPUFMTF9EUklWRVJTJnNlbGVjdGVkRGF5PTIwMjUtMTEtMDMmc2VydmljZUFyZWFJZD1kNDU5Nzg4Yi02YTczLTQ4ZjktYTcxMy04MWFmYTBjNTliNjYmdHJhbnNwb3J0ZXI9QUxMX0RSSVZFUlMiLCJyZWZlcnJlckRvbWFpbiI6ImxvZ2lzdGljcy5hbWF6b24uZnIiLCJzdGFydCI6MTc2MjE4NjM5MDk4MX19; x-acbfr=S6nVDF7DBQis7psHiQBPgmunzuEqBFBW8@wFhyUTnVbf5cMryEWf87QwajPPGFZC; session-token=JnMCUjDnJVFwqeoHOtID5/Fa0ri1WAZcBIi5LjOenMmvPQOGWuaoDaeF/jpuYFVA2MYEBdY+jdwRSGT9+H4cszhjIrPISZ1PaKxHcgBTw0DuK/yYaf50cEjEKMJsd9XNiTwnb0C7wbL6frknvZRJsuo+O+UYrHWpd7AKkd8SyWdWya9AzLdXOgfumuGaLCTcP/mqNlSUuD+DnrpZkI++ZwRyUhLPPaxeO/TOodQBopEKjrQEKnn3DaTHN5aAVkbH1w1Jvo+o0FGtgAwThG4695QiWA1ItDeyKu/iJH0bJWbhKSf3Ela76RPwBfjp0I7I9mBkGgbrp9bi4CdYYz3iNfHzKlNQBqUssTKUkoOeZrx53Dqct3oZ4+xYRSUhoR4b',
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
    all_route_ids = []

    for itinerary in data.get('rmsRouteSummaries', []):
        route_id = itinerary.get('routeId')  # directement ici
        if route_id:
            all_route_ids.append(route_id)

    prefixed_route_links = [
        f"https://logistics.amazon.fr/operations/execution/api/routes/{route_id}" 
        for route_id in all_route_ids
    ]

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
