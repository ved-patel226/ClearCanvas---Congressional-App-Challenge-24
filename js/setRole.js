console.log('setRole.js loaded');

function setrole(role) {
    document.getElementById('roleInput').value = role;
    console.log(document.getElementById('roleInput').value);
    document.getElementById('roleForm').submit();
}
