function iniciarMap() {
    var coord = { lat: -33.0089525, lng: -71.5496488 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}