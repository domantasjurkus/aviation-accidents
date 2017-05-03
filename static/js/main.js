var noDBString = 'Uh oh, it appears the database has not been generated - be sure to run `cd data` and `python data/main.py`'

function createMap(databaseGenerated) {
  if (!databaseGenerated) {
    document.getElementById('container').innerHTML = noDBString;
    return;
  }

  var map = new Datamap({
    element: document.getElementById('container'),
    fills: {
      defaultFill: "#ABDDA4",
      red: "#dd0000"
    },
    setProjection: function(element) {
      var projection = d3.geo.equirectangular()
        .center([2, 45])
        .rotate([0, 0])
        .scale(1200)
        .translate([element.offsetWidth / 2, element.offsetHeight / 2]);
      var path = d3.geo.path()
        .projection(projection);

      return {path: path, projection: projection};
    },
  });

  addBubbleData(map);  
}

function addBubbleData(map) {
  $.ajax({
    'url': '/france',
    success: function(data) {
      var bubbleArray = data.map(function(gid) {
        var o = {
          name: gid.date,
          latitude: parseFloat(gid.latitude),
          longitude: parseFloat(gid.longitude),
          fatalities: gid.total_fatal_injuries,
          radius: 3 + 1.7 * gid.total_fatal_injuries,
          fillKey: 'red'
        }

        return o;
      });
      map.bubbles(bubbleArray, {
        popupTemplate: function(geo, data) {
          return "<div class='hoverinfo'>"+data.name+" Fatalities: "+data.fatalities+"</div>";
        }
      });
    }
  })
}