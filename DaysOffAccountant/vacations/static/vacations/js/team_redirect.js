function redirectToTeam(event) {
    event.preventDefault();
    const teamName = document.getElementById('team-select').value;
    window.location.href = '/teams/' + encodeURIComponent(teamName);
}