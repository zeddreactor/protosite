import {scaleLinear} from "d3-scale";
import "d3";

var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
    message2: 'Waaaaaay',
  }
});

var app3 = new Vue({
  el: '#app-3',
  data: {
    seen: true
  }
});

var svg = d3.select('svg')
    .attr("width", 500)
    .attr("height", 500)
    .attr("class", "bar-chart");
// var hr = d3.histogram([5, 6, 7]);
