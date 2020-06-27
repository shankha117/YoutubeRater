<template>
  <div class="main-text" v-if="videodetail.title != null">
    <div class="row">
      <div class="col-md-10">
        <p class="mb-3">
          <span class="bodyp">Title :</span>
          {{ videodetail.title }}
        </p>
        <p>
          <span class="bodyp">Description :</span>
          {{ videodetail.title }}
        </p>
        <p>Rating : {{ videodetail.rating_average }}</p>
        <p>Comments : {{ videodetail.comments_list }}</p>

        <iframe
          width="400"
          height="215"
          :src="videodetail.url"
          frameborder="0"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>

        <p>Category: {{ videodetail.category }}</p>
      </div>
    </div>
    <form id="formvideo" @submit.prevent="giveRating()">
      <p>
        <label for="stars">Give a Rating</label>
        <input class="ml-2" type="text" name="stars" id="stars" v-model="stars" />
      </p>
      <p>
        <label for="comments">Comments</label>
        <input class="ml-2" type="text" name="comments" id="comments" v-model="comments" />
      </p>
      <p>
        <input class="btn-primary" type="submit" value="Submit Rating" />
      </p>
    </form>
    <button class="btn-sm btn-danger mt-2 mb-3" v-on:click="videoDelete()">Delete Video</button>
  </div>
</template>

<script>
import axios from "axios";
import { TokenService } from "../storage/service";

export default {
  name: "VideoDetails",
  components: {},
  props: {
    videodetail: {}
  },
  data() {
    return {
      token: "",
      stars: "",
      comments: ""
    };
  },
  methods: {
    videoDelete() {
      console.log(this.token);
      let axiosConfig = {
        headers: {
          Authorization: "Token " + this.token
        }
      };
      axios
        .delete(
          `http://127.0.0.1:8000/api/v1/videos/${this.videodetail.id}`,
          axiosConfig
        )
        .then(res => {
          console.log(res.data);
          this.$emit("updated");
        })
        .catch(err => console.log(err));
    },
    giveRating() {
      console.log(this.videodetail.id);
      var postData = {
        stars: this.stars,
        comments: this.comments
      };
      let axiosConfig = {
        headers: {
          Authorization: "Token " + this.token
        }
      };
      axios
        .post(
          `http://127.0.0.1:8000/api/v1/videos/${this.videodetail.id}/rate_video/`,
          postData,
          axiosConfig
        )
        .then(res => {
          console.log(res.data);
          this.$emit("updated");
        })
        .catch(err => console.log(err));
    }
  },
  created() {
    this.token = TokenService.getToken();
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Muli&display=swap");

.main-text {
  font-family: "Muli", sans-serif;
  font-size: 20px;
  color: black;
}

.bodyp {
  color: blue;
  font-family: "Muli", sans-serif;
}
</style>

