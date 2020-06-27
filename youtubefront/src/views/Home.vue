<template>
  <div class="home">
    <h4>Welcome to Youtube Rater</h4>
    <br />
    <br />
    <ListVideos />
  </div>
</template>

<script>
// @ is an alias to /src
import ListVideos from "@/components/ListVideos.vue";

export default {
  name: "Home",
  components: {
    ListVideos
  }
};
</script>
