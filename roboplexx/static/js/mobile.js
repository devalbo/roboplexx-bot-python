
var left_control = null,
    right_control = null;
var left_control_ctx = null,
    right_control_ctx = null;

var speedLeft = null,
    speedRight = null;
var lastSentSpeedLeft = null,
    lastSentSpeedRight = null;

var gaugeLeft = null,
    gaugeRight = null;
var mouseX, mouseY,
    touchable = 'createTouch' in document,
    touches = [],
    left_touches = [],
    right_touches = [];

function init()
{
    setup_page();
    setInterval(process_gauges, 1000/35);
//    setInterval(sendUpdatedSpeeds, 1000/333);

    if(touchable) {
//        left_control.addEventListener( 'touchstart', onLeftTouchStart, false );
//        left_control.addEventListener( 'touchmove', onLeftTouchMove, false );
//        left_control.addEventListener( 'touchend', onLeftTouchEnd, false );
//
//        right_control.addEventListener( 'touchstart', onRightTouchStart, false );
//        right_control.addEventListener( 'touchmove', onRightTouchMove, false );
//        right_control.addEventListener( 'touchend', onRightTouchEnd, false );

        left_control.addEventListener( 'touchstart', onTouchStart, false );
        left_control.addEventListener( 'touchmove', onTouchMove, false );
        left_control.addEventListener( 'touchend', onTouchEnd, false );

        right_control.addEventListener( 'touchstart', onTouchStart, false );
        right_control.addEventListener( 'touchmove', onTouchMove, false );
        right_control.addEventListener( 'touchend', onTouchEnd, false );

        window.onorientationchange = setup_page;
        window.onresize = setup_page;

    } else {

        left_control.addEventListener( 'mousemove', onMouseMove, false );
        right_control.addEventListener( 'mousemove', onMouseMove, false );
    }

}

function setup_page()
{
    left_control = document.getElementById('left_control');
    left_control.width = window.innerWidth / 10;
    left_control.height = window.innerHeight;

    left_control_ctx = left_control.getContext('2d');
    left_control_ctx.strokeStyle = "#ffffff";
    left_control_ctx.lineWidth = 2;

    right_control = document.getElementById('right_control');
    right_control.width = window.innerWidth / 10;
    right_control.height = window.innerHeight;

    right_control_ctx = right_control.getContext('2d');
    right_control_ctx.strokeStyle = "#ffffff";
    right_control_ctx.lineWidth = 2;
}

function process_gauges()
{
    left_control_ctx.clearRect(0, 0, left_control.width, left_control.height);
    right_control_ctx.clearRect(0, 0, right_control.width, right_control.height);

    left_control_ctx.beginPath();
    left_control_ctx.moveTo(0, left_control.height / 2);
    left_control_ctx.lineTo(left_control.width, left_control.height / 2);
    left_control_ctx.stroke();

    right_control_ctx.beginPath();
    right_control_ctx.moveTo(0, right_control.height / 2);
    right_control_ctx.lineTo(right_control.width, right_control.height / 2);
    right_control_ctx.stroke();

//    if(touchable) {

        var theTouch = null;
        var leftTouch = null;
        var rightTouch = null;

        // topmost left-side and right-side touches get to be the speed touches
        for (var i=0; i<touches.length; i++) {
            var touch = touches[i];
            if (touch.clientX >= left_control.offsetLeft &&
                touch.clientX <= (left_control.offsetLeft + left_control.offsetWidth)
                )
            {
                leftTouch = touch;
                speedLeft = ((((left_control.height / 2) - leftTouch.clientY) / (left_control.height / 2))  * 100);
                gaugeLeft = leftTouch.clientY;
            }
            if (touch.clientX >= right_control.offsetLeft &&
                touch.clientX <= (right_control.offsetLeft + right_control.offsetWidth)
                )
            {
                rightTouch = touch;
                speedRight = ((((right_control.height / 2) - rightTouch.clientY) / (right_control.height / 2))  * 100);
                gaugeRight = rightTouch.clientY;
            }
        }


//        var theSpeed = null;
//        var theGauge = null;
//        if (theTouch != null) {
//            theGauge = theTouch.clientY;
//            if (theTouch.clientY <= (gauge_ctrl.height / 2)) {
//                theSpeed = ((((gauge_ctrl.height / 2) - theTouch.clientY) / (gauge_ctrl.height / 2))  * 100);
//            } else {
//                theSpeed = (((gauge_ctrl.height / 2) - theTouch.clientY) / (gauge_ctrl.height / 2)) * 100;
//            }
//            if (gauge_ctrl == left_control) {
//                gaugeLeft = theTouch.clientY;
//            } else if (gauge_ctrl == right_control) {
//                gaugeRight = theTouch.clientY;
//            }
//        }

        left_control_ctx.fillStyle="#9acd32";
        right_control_ctx.fillStyle="#9acd32";
        if (speedLeft < 0) {
            left_control_ctx.fillStyle="#CD0000";
        }
        if (speedRight < 0) {
            right_control_ctx.fillStyle="#CD0000";
        }

        if (gaugeLeft != null) {
            left_control_ctx.fillRect(0, gaugeLeft, left_control.width, (left_control.height / 2) - gaugeLeft);
            $('#status_left').text('Left:' + speedLeft.toFixed(0) + "%");
        }
        if (gaugeRight != null) {
            right_control_ctx.fillRect(0, gaugeRight, right_control.width, (right_control.height / 2) - gaugeRight);
            $('#status_right').text('Right:' + speedRight.toFixed(0) + "%");
        }

//        c.fillStyle    = '#00f';
//        c.font         = 'italic 30px sans-serif';
//        c.textBaseline = 'top';

//    } else {
//
//        c.fillStyle	 = "white";
//        c.fillText("mouse : "+mouseX+", "+mouseY, mouseX, mouseY);

//    }

}

//function process_gauges() {
//    process_gauge(left_control, left_touches);
//    process_gauge(right_control, right_touches);
//}

////function process_gauge(gauge_ctrl, touches)
//function process_gauge(gauge_ctrl)
//{
//    var c = gauge_ctrl.getContext('2d');
//    c.clearRect(0, 0, gauge_ctrl.width, gauge_ctrl.height);
//
////    c.beginPath();
////    c.moveTo(gauge_ctrl.width / 2, 0);
////    c.lineTo(gauge_ctrl.width / 2, gauge_ctrl.height);
////    c.stroke();
//
//    c.beginPath();
//    c.moveTo(0, gauge_ctrl.height / 2);
//    c.lineTo(gauge_ctrl.width, gauge_ctrl.height / 2);
//    c.stroke();
//
////    if (gauge_ctrl == left_control) {
////
////    } else if (gauge_ctrl == right_control) {
////
////    }
//
////    if(touchable) {
//
//        var theTouch = null;
//        var leftTouch = null;
//        var rightTouch = null;
//
////        // topmost touches get to be the speed touches
////        for(var i=0; i < touches.length; i++) {
////            var touch = touches[i];
////
////            if (theTouch == null || touch.clientY > theTouch.clientY) {
////                theTouch = touch;
////            }
////        }
//
//        // topmost left-side and right-side touches get to be the speed touches
//        for(var i=0; i<touches.length; i++)
//        {
//            var touch = touches[i];
//            if (touch.clientX >= left_control.offsetLeft &&
//                touch.clientX <= (left_control.offsetLeft + left_control.offsetWidth)
//                )
//            {
//                leftTouch = touch;
//            }
//            if (touch.clientX >= right_control.offsetLeft &&
//                touch.clientX <= (right_control.offsetLeft + right_control.offsetWidth)
//                )
//            {
//                rightTouch = touch;
//            }
//
//            if (leftTouch != null) {
//                $('#status_left').text('Left:' + leftTouch.clientY);
//            }
//            if (rightTouch != null) {
//                $('#status_right').text('Right:' + rightTouch.clientY);
//            }
//
//
////            if (gauge_ctrl == left_control) {
//////                if (leftTouch == null || touch.clientY > leftTouch.clientY) {
//////                    leftTouch = touch;
//////                    theTouch = touch;
//////                }
////            } else if (gauge_ctrl == right_control) {
//////                if (touch.clientX > right_control.position().left &&
//////                    touch.clientX < right_control.position().right &&
//////                    touch.clientY > right_control.position().bottom &&
//////                    touch.clientY < right_control.position().top
//////                    )
//////                {
//////                    alert("In right");
//////                    rightTouch = touch;
//////                }
////                if (rightTouch == null || touch.clientY > rightTouch.clientY) {
////                    rightTouch = touch;
////                    theTouch = touch;
////                }
////            }
//        }
//
//
//        var theSpeed = null;
//        var theGauge = null;
//        if (theTouch != null) {
//            theGauge = theTouch.clientY;
//            if (theTouch.clientY <= (gauge_ctrl.height / 2)) {
//                theSpeed = ((((gauge_ctrl.height / 2) - theTouch.clientY) / (gauge_ctrl.height / 2))  * 100);
//            } else {
//                theSpeed = (((gauge_ctrl.height / 2) - theTouch.clientY) / (gauge_ctrl.height / 2)) * 100;
//            }
//            if (gauge_ctrl == left_control) {
//                gaugeLeft = theTouch.clientY;
//            } else if (gauge_ctrl == right_control) {
//                gaugeRight = theTouch.clientY;
//            }
//        }
//
//        c.fillStyle="#9acd32";
//
//        if (gauge_ctrl == left_control) {
//            speedLeft = theSpeed;
//            c.fillRect(0, gaugeLeft, gauge_ctrl.width, (gauge_ctrl.height / 2) - gaugeLeft);
//        } else if (gauge_ctrl == right_control) {
//            speedRight = theSpeed;
//            c.fillRect(0, gaugeRight, gauge_ctrl.width, (gauge_ctrl.height / 2) - gaugeRight);
//        }
////        speedStr = '?';
////        if (speedLeft != null) {
////            speedLeftStr = speedLeft.toFixed(0) + '%';
////        }
//
//        c.fillStyle    = '#00f';
//        c.font         = 'italic 30px sans-serif';
//        c.textBaseline = 'top';
////        c.fillText('Speed:' + speedStr, 0, 0);
//
////        for (var touch in [leftTouch, rightTouch]) {
//            if (theTouch != null) {
//                c.beginPath();
//                c.fillStyle = "white";
////                c.fillText("speed: " + speedLeft);
//
//                c.beginPath();
//                c.strokeStyle = "cyan";
//                c.lineWidth = "6";
//                c.arc(theTouch.clientX, theTouch.clientY, 40, 0, Math.PI*2, true);
//                c.stroke();
//            }
////        }
//
////    } else {
////
////        c.fillStyle	 = "white";
////        c.fillText("mouse : "+mouseX+", "+mouseY, mouseX, mouseY);
//
////    }
//
//}

function sendUpdatedSpeeds() {
    if (speedLeft != lastSentSpeedLeft ||
        speedRight != lastSentSpeedRight)
    {
        $.post("motors", { left_speed: speedLeft, right_speed: speedRight } );
        lastSentSpeedLeft = speedLeft;
        lastSentSpeedRight = speedRight;
    }
}


/*
 *	Touch event (e) properties :
 *	e.touches: 			Array of touch objects for every finger currently touching the screen
 *	e.targetTouches: 	Array of touch objects for every finger touching the screen that
 *						originally touched down on the DOM object the transmitted the event.
 *	e.changedTouches	Array of touch objects for touches that are changed for this event.
 *						I'm not sure if this would ever be a list of more than one, but would
 *						be bad to assume.
 *
 *	Touch objects :
 *
 *	identifier: An identifying number, unique to each touch event
 *	target: DOM object that broadcast the event
 *	clientX: X coordinate of touch relative to the viewport (excludes scroll offset)
 *	clientY: Y coordinate of touch relative to the viewport (excludes scroll offset)
 *	screenX: Relative to the screen
 *	screenY: Relative to the screen
 *	pageX: Relative to the full page (includes scrolling)
 *	pageY: Relative to the full page (includes scrolling)
 */
function onTouchStart(e) {
    touches = e.touches;
}

function onTouchMove(e) {
    // Prevent the browser from doing its default thing (scroll, zoom)
    e.preventDefault();
    touches = e.touches;
}

function onTouchEnd(e) {
    touches = e.touches;
}

function onLeftTouchStart(e) {
    left_touches = e.touches;
}

function onLeftTouchMove(e) {
    // Prevent the browser from doing its default thing (scroll, zoom)
    e.preventDefault();
    left_touches = e.touches;
}

function onLeftTouchEnd(e) {
    left_touches = e.touches;
}

function onRightTouchStart(e) {
    right_touches = e.touches;
}

function onRightTouchMove(e) {
    // Prevent the browser from doing its default thing (scroll, zoom)
    e.preventDefault();
    right_touches = e.touches;
}

function onRightTouchEnd(e) {
    right_touches = e.touches;
}

function onMouseMove(event) {
    mouseX = event.offsetX;
    mouseY = event.offsetY;
}
