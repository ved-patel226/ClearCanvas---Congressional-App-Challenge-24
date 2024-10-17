document.addEventListener('DOMContentLoaded', () => {
    const image = document.getElementById('image');
    const canvas = document.getElementById('canvas');
    const schoolContainer2 = document.getElementById('after');
    const schoolContainer = document.querySelector('.school-container');
    const csrfToken = document.getElementById('csrf_token').value;

    schoolContainer2.style.display = 'none';

    var count = 0;

    image.addEventListener('click', (event) => {
        if (count === 1) {
            schoolContainer.style.display = 'none';
            schoolContainer2.style.display = 'block';

            return;
        }

        count += 1;
        
        console.log(count);

        const x = event.offsetX - 10;
        const y = event.offsetY - 10;

        const circle = document.createElement('div');
        circle.classList.add('circle');
        circle.style.left = `${x}px`;
        circle.style.top = `${y}px`;

        canvas.appendChild(circle);

        fetch('/coordinates', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // csrf token is needed for some reason
            },
            body: JSON.stringify({ x: x, y: y }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        .catch(error => console.error('Error:', error));
    });
});
