function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            showPosition,
            handleLocationError,
            {
                enableHighAccuracy: true,  // Optional, use high-accuracy mode if available
                timeout: 5000,            // Optional, set a timeout (milliseconds)
                maximumAge: 0             // Optional, don't use a cached position
            }
        );
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    console.log("Latitude: " + position.coords.latitude);
    console.log("Longitude: " + position.coords.longitude);

    // Call the function to send the position to the server
    sendPositionToServer(position);
}

function sendPositionToServer(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    // Create a data object with the geolocation information
    const data = {
        latitude: latitude,
        longitude: longitude
    };

    // Make a POST request to your Django server
    fetch('handle_geolocation/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function handleLocationError(error) {
    console.error('Error getting location:', error.message);
}

// Trigger the geolocation when the page loads
getLocation();
