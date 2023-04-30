(function ($) {
  

  $.fn.enableCellNavigation = function () {
    var arrow = {
      left: 37,
      up: 38,
      right: 39,
      down: 40,
    };

    
    this.find("select,input").keydown(function (e) {
        // shortcut for key other than arrow keys
        console.log(e)
        if (
          $.inArray(e.which, [arrow.left, arrow.up, arrow.right, arrow.down]) < 0
        ) {
          return;
        }
  
        var input = e.target;
        var td = $(e.target).closest("td");
        var moveTo = null;
  
        switch (e.which) {
          case arrow.left: {
            if (input.selectionStart == 0) {
              moveTo = td.prev("td:has(input,textarea,select)");
            }
            break;
          }
          case arrow.right: {
            if (input.selectionEnd == input.value.length) {
              moveTo = td.next("td:has(input,textarea,select)");
            }
            break;
          }
  
          case arrow.up:
          case arrow.down: {
            var tr = td.closest("tr");
            var pos = td[0].cellIndex;
  
            var moveToRow = null;
            if (e.which == arrow.down) {
              moveToRow = tr.next("tr");
            } else if (e.which == arrow.up) {
              moveToRow = tr.prev("tr");
            }
  
            if (moveToRow.length) {
              moveTo = $(moveToRow[0].cells[pos]);
            }
  
            break;
          }
        }
  
        if (moveTo && moveTo.length) {
          e.preventDefault();
  
          moveTo.find("input,select").each(function (i, input) {
            input.focus();
            input.select();
          });
        }
      });
  };


})(jQuery);