function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 37.5665, lng: 126.9780 }, // 기본 중심 좌표를 서울로 설정
      zoom: 10,
  });

  // 정보 창 객체 생성
  const infoWindow = new google.maps.InfoWindow();
  // 지도 경계 조정을 위한 LatLngBounds 객체 생성
  const bounds = new google.maps.LatLngBounds();
  fetch('/get_locations') // Flask 서버에서 위치 데이터를 가져옴
      .then(response => response.json())
      .then(data => {
          data.forEach(locationArray => {
              let [hostname, country_name, region, city, postal,latitude, longitude, ban_start_time, access_time] = locationArray; // 배열 구조 분해 할당을 사용
              latitude = parseFloat(latitude)
              longitude = parseFloat(longitude)
              // 마커 생성
              const marker = new google.maps.Marker({
                  position: { lat: latitude, lng: longitude },
                  map: map,
                  title: hostname,
              });

              // 경계를 마커의 위치로 확장
              bounds.extend(marker.position);

              // 마커 클릭 이벤트 리스너 추가
              marker.addListener('click', () => {
                  // 정보 창에 hostname 표시
                  infoWindow.setContent(hostname);
                  infoWindow.open(map, marker);

                  // 지도 중심을 마커의 위치로 이동
                  map.panTo(marker.position);
              });
          });

          // 모든 마커를 포함하도록 지도 경계 조정
          map.fitBounds(bounds);
      })
      .catch(error => console.error('Error:', error));
}