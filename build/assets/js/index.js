/* eslint-disable no-undef */
 (function ($) {

  'use strict';
  $.fn.enableCellNavigation = function () {
    var arrow = {
      left: 37,
      up: 38,
      right: 39,
      down: 40,
    };

    // select all on focus
    // works for input elements, and will put focus into
    // adjacent input or textarea. once in a textarea,
    // however, it will not attempt to break out because
    // that just seems too messy imho.
    this.find("input").keydown(function (e) {
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
            moveTo = td.prev("td:has(input,textarea)");
          }
          break;
        }
        case arrow.right: {
          if (input.selectionEnd == input.value.length) {
            moveTo = td.next("td:has(input,textarea)");
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

        moveTo.find("input,textarea").each(function (i, input) {
          input.focus();
          input.select();
        });
      }
    });
  };
})(jQuery);

// use the plugin
$(function () {
  $("#people").enableCellNavigation();
});