function getNewToken() {
    /*
    data = {
        'client_id': self.client_id,
        'client_secret': self.client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': self.refresh_token
    }
    response = requests.post(
        'https://accounts.spotify.com/api/token', data=data)

    # GET TOKEN:
    response = response.json()
    self.token = response["access_token"]
    */
    return "abcd"
}

$(document).ready(function () {
        
    window.onSpotifyWebPlaybackSDKReady = () => {
        const token = 'MYTOKEN';
        const player = new Spotify.Player({
          name: 'Web Playback SDK Quick Start Player',
          getOAuthToken: cb => { cb(token); }
        });
    
        // Error handling
        player.addListener('initialization_error', ({ message }) => { console.error(message); });
        player.addListener('authentication_error', ({ message }) => { console.error(message); });
        player.addListener('account_error', ({ message }) => { console.error(message); });
        player.addListener('playback_error', ({ message }) => { console.error(message); });
    
        // Playback status updates
        player.addListener('player_state_changed', state => { console.log(state); });
    
        // Ready
        player.addListener('ready', ({ device_id }) => {
          console.log('Ready with Device ID', device_id);
        });
    
        // Not Ready
        player.addListener('not_ready', ({ device_id }) => {
          console.log('Device ID has gone offline', device_id);
        });
    
        // Connect to the player!
        player.connect();
      };

});
