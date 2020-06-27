<template>
  <div class="home">
    <div class="col-md-12 mb-5" v-if="createnew">
      <CreateVideo v-on:updated="getVideos()"/>
    </div>
    <div class="row">
      <div class="col-md-5 text-center nicefont">

        <form 
        @submit.prevent="showform()">
          <input class="btn-sm btn-primary mb-3 btn-center" type="submit" value="Create New Video" id="showform"/>
        </form>




        <p v-for="item in videos" :key="item.id">
          {{ item.title }}
          <br />
          Rating:
          {{ item.rating_average }}
          <br />
          <ul class="list-inline">
            <li class="col-md-12 text-center" v-for="comment in item.comments_list" :key="comment">
            {{ comment }}
          </li>
          </ul>
          <button class="btn-sm btn-primary mt-2 mb-3" @click="VideoDetails(item)">Details</button>
        </p>
      </div>

      <div class="col-md-6 text-center">
          <VideoDetails v-bind:videodetail="videodetail" v-on:updated="getVideos()"></VideoDetails>
      </div>



    </div>
  </div>
</template>

<script>
import axios from "axios";
import CreateVideo from './CreateVideo.vue'
import VideoDetails from './VideoDetails.vue'


export default {
  name: "Home",
  components: {
    VideoDetails,
    CreateVideo
  },

  data() {
    return {
      videos: [],
      videodetail: Object,
      createnew: Boolean
    };
  },
  methods: {
    getVideos() {
      console.log("UPDATING VIDEO");
      axios
        .get("http://localhost:8000/api/v1/videos/")
        .then(res => {
          this.videos = res.data;
          console.log(this.videos);
          
          console.log("data stored");
        })
        .catch(err => console.log(err));
    },

    VideoDetails(video){
      this.videodetail = video;
      console.log(this.videodetail);
      
    },
    showform(){
      this.createnew = ! this.createnew
    },
    updateVideos() {

      console.log("UPDATING VIDEO");
      

      this.timer = setTimeout(() => {

      axios
      .get("http://127.0.0.1:8000/api/v1/videos/")
      .then(res => (this.videos = res.data))
      .catch(err => console.log(err));
        }, 600);
    }
    
    },

  created() {
    this.getVideos();
    this.createnew = false;
  }
};
</script>

<style scopped>
@import url("https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@300&display=swap");

.nicefont {
  font-family: "Source Code Pro", monospace;
  font-size: 26px;
}
</style>