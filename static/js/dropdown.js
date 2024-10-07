const schoolInput = document.getElementById('school_name');
const suggestions = document.getElementById('suggestions');

const schoolInput2 = document.getElementById('school_name_2');
const suggestions2 = document.getElementById('suggestions_2');


let lastValidSchool = '';

schoolInput.addEventListener('input', function() {
    const query = this.value;

    if (query.length > 0) {
        // api call to fetch schools
        fetch(`/search_schools?query=${query}`)
            .then(response => response.json())
            .then(data => {
                suggestions.innerHTML = '';
                suggestions.style.display = 'none';

                data.forEach(school => {
                    const li = document.createElement('li');
                    li.textContent = `${school[0]} - ${school[1]}`;
                    li.onclick = function() {
                        schoolInput.value = `${school[0]} - ${school[1]}`;
                        lastValidSchool = `${school[0]} - ${school[1]}`;
                        suggestions.innerHTML = '';
                        suggestions.style.display = 'none';
                    };
                    suggestions.appendChild(li);
                });

                if (data.length > 0) {
                    suggestions.style.display = 'block';
                } else {
                    suggestions.style.display = 'none';
                }
            })
            .catch(error => console.error('Error fetching schools:', error));
    } else {
        suggestions.style.display = 'none';
    }
});

document.addEventListener('click', function(event) {
    if (!schoolInput.contains(event.target)) {
        suggestions.style.display = 'none';
    }
});

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    if (!lastValidSchool || schoolInput.value !== lastValidSchool) {
        event.preventDefault(); // stop form submision
        alert('Please select a valid school from the dropdown.'); // alert
        schoolInput.value = '';
        suggestions.innerHTML = '';
        suggestions.style.display = 'none';
    }
});


schoolInput2.addEventListener('input', function() {
    const query = this.value;

    if (query.length > 0) {
        // api call to fetch schools
        fetch(`/search_schools?query=${query}`)
            .then(response => response.json())
            .then(data => {
                suggestions2.innerHTML = '';
                suggestions2.style.display = 'none';

                data.forEach(school => {
                    const li = document.createElement('li');
                    li.textContent = `${school[0]} - ${school[1]}`;
                    li.onclick = function() {
                        schoolInput2.value = `${school[0]} - ${school[1]}`;
                        lastValidSchool = `${school[0]} - ${school[1]}`;
                        suggestions2.innerHTML = '';
                        suggestions2.style.display = 'none';

                        // Automatically submit the form after selecting a school
                        document.getElementById('schoolForm').submit();
                    };
                    suggestions.appendChild(li);
                });

                if (data.length > 0) {
                    suggestions.style.display = 'block';
                } else {
                    suggestions.style.display = 'none';
                }
            })
            .catch(error => console.error('Error fetching schools:', error));
    } else {
        suggestions.style.display = 'none';
    }
});

document.addEventListener('click', function(event) {
    if (!schoolInput2.contains(event.target)) {
        suggestions2.style.display = 'none';
    }
});
