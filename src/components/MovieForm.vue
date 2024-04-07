<script setup>

import { ref, onMounted } from "vue";
let csrf_token = ref(""); 
let fetchResponseType = ref("")
let fetchResponse = ref("")
    


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
    fetchResponse.value = data
            
            if(data.hasOwnProperty('errors')) {
                fetchResponseType.value = "danger"
            } else {
                fetchResponseType.value = "success"
            }
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

            <div v-if="fetchResponseType == 'success'" class="alert alert-success">{{ fetchResponse.message }}</div>
            <div v-if="fetchResponseType == 'danger'" class="alert alert-danger">
                <ul>
                    <li v-for="error in fetchResponse.errors" >{{ error }}</li>
                </ul>
            </div>

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
                <input type="file" id="poster" name="poster" class="form-control" accept=".jpg,.png" />
            </div>

            <button>Submit</button>
        </form>
    </div>

</template>

<style>
* { 
    -moz-box-sizing: border-box; 
    -webkit-box-sizing: border-box; 
    box-sizing: border-box; 
}
form{
    margin: 25px;
}
label{
    display: block;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
}
input, textarea{
    max-width: 700px;
    width: 100%;
}
#poster{
    border: 1px solid black;
}
</style>
