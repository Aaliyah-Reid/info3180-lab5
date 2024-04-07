<script setup>

import { ref, onMounted } from "vue";
let csrf_token = ref(""); 
// let fetchResponseType = ref("")
// let fetchResponse = ref("")
    


function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    console.log(data);
    csrf_token.value = data.csrf_token;
    })
}

onMounted(() => {
 getCsrfToken();
}); 


function saveMovie(){



    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);


    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
        'X-CSRFToken': csrf_token.value
        }
    })

    .then(function (response) {
    return response.json();
    })

    .then(function (data) {
    // display a success message
    console.log(data);
    })
    .catch(function (error) {
    console.log(error);
    });

}



</script>

<template>
    <div class="form-container">
        <form  @submit.prevent="saveMovie"  id="movieForm">
            <h1>Movie Upload </h1>

            <div class="form-group mb-3">
                <label for="title" class="form-label">Movie Title</label>
                <input type="text" name="title" class="form-control" />
            </div>

            <div class="form-group mb-3">
                <label for="descritption"  class="form-label">Movie Description</label>
                <textarea type="text" name="description" class="form-control"></textarea>
            </div>
            
            <div class="form-group mb-3">
                <label for="poster" class="form-label">Movie Poster</label>
                <input type="file" id="poster" name="poster" class="form-control" accept=".jpg" />
            </div>

            <button>Submit</button>
        </form>
    </div>

</template>