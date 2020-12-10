// var dataSource = {
//   datasets: [
//    {
//       data: [],
//       backgroundColor:[],
// }
// ],

// labels:[ ]
// };

// function createChart(){
//  var ctx = document.getElementById('myChart').getContext('2d');
//  var myChart  = new Chart(ctx, {

//      type: 'pie',
//      data: dataSource
//  });
// }

// function getCurrentUpdates(){
// axios.get('http://localhost:4000/CurrentUpdates')
// .then(function(res){
// console.log(res);
// for(var i = 0; i < res.data.length; i++){
// dataSource.datasets[0].data[i] = res.data[i].covid;
// dataSource.labels[i] = res.data[i].title;
// dataSource.datasets[0].backgroundColor[i] = res.data[i].color;

// }
// createChart();

// });
// }

// getCurrentUpdates();

