window.initMap = function () {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 37.5400456, lng: 126.9921017 },
    zoom: 10,
  });

  const ips = [
    { name: "코엑스몰", lat: 37.5115557, lng: 127.0595261 },
    { name: "고투몰", lat: 37.5062379, lng: 127.0050378 },
    { name: "동대문시장", lat: 37.566596, lng: 127.007702 },
    { name: "IFC몰", lat: 37.5251644, lng: 126.9255491 },
    { name: "롯데월드타워몰", lat: 37.5125585, lng: 127.1025353 },
    { name: "명동지하상가", lat: 37.563692, lng: 126.9822107 },
    { name: "타임스퀘어", lat: 37.5173108, lng: 126.9033793 },
  ];

  const bounds = new google.maps.LatLngBounds();
  const infowindow = new google.maps.InfoWindow();

  ips.forEach(({label, name, lat, lng}) =>{
    const marker = new google.maps.Marker({
      position:{lat, lng},
      map
    });
    bounds.extend(marker.position);

    marker.addListener("click", () => {
      map.panTo(marker.position);
      infowindow.setContent(name);
      infowindow.open({
        anchor: marker,
        map,
      });
    });
  });
  map.fitBounds(bounds);
};