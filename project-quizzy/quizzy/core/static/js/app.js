the_button.addEventListener('click', load_massage);

function load_massage(event){
    var context = encodeURIComponent(document.getElementById('the_area').value);
    url = "hola/" + '?context=' + context
    fetch(url).then(response => response.json()).then(function(data){
        // Create new element
        const new_element = document.createElement("div");
        // Get and append to container
        const container = document.getElementById("pruba-text");
        new_element.textContent = data['context'];
        container.appendChild(new_element);
})};