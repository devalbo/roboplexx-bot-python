var VirtualJoystick = function (opts) {
    opts = opts || {};
    this._container = opts.container || document.body;
    this._stickEl = opts.stickElement || this._buildJoystickStick();
    this._baseEl = opts.baseElement || this._buildJoystickBase();
    this._mouseSupport = 'mouseSupport' in opts ? opts.mouseSupport : false;
    this._range = opts.range || 60;

    this._container.style.position = "relative";
//    this._baseEl.style.position = "absolute";
    this._baseEl.style.left = (this._container.width / 2 - this._baseEl.width / 2) + "px";
    this._baseEl.style.top = (this._container.height / 2 - this._baseEl.height / 2) + "px";

    this._stickEl.style.position = "relative";
//    this._stickEl.style.display = "none";

    this._container.appendChild(this._baseEl);
    this._container.appendChild(this._stickEl);

    this._pressed = false;
//    this._baseX = this._container.width / 2;
//    this._baseY = this._container.height / 2;
    this._baseX = (this._baseEl.width / 2);
    this._baseY = this._baseEl.height / 2;
//    this._baseX = 300;
//    this._baseY = 200;
    this._stickX = 0;
    this._stickY = 0;

    __bind = function (fn, me) { return function () { return fn.apply(me, arguments); }; };
    this._$onTouchStart = __bind(this._onTouchStart, this);
    this._$onTouchEnd = __bind(this._onTouchEnd, this);
    this._$onTouchMove = __bind(this._onTouchMove, this);
    this._container.addEventListener('touchstart', this._$onTouchStart, false);
    this._container.addEventListener('touchend', this._$onTouchEnd, false);
    this._container.addEventListener('touchmove', this._$onTouchMove, false);
    if (this._mouseSupport) {
        this._$onMouseDown = __bind(this._onMouseDown, this);
        this._$onMouseUp = __bind(this._onMouseUp, this);
        this._$onMouseMove = __bind(this._onMouseMove, this);
        this._container.addEventListener('mousedown', this._$onMouseDown, false);
        this._container.addEventListener('mouseup', this._$onMouseUp, false);
        this._container.addEventListener('mousemove', this._$onMouseMove, false);
    }
}

VirtualJoystick.prototype.destroy	= function()
{
	this._container.removeChild(this._baseEl);
	this._container.removeChild(this._stickEl);

	this._container.removeEventListener( 'touchstart'	, this._$onTouchStart	, false );
	this._container.removeEventListener( 'touchend'		, this._$onTouchEnd	, false );
	this._container.removeEventListener( 'touchmove'	, this._$onTouchMove	, false );
	if( this._mouseSupport ){
		this._container.removeEventListener( 'mouseup'		, this._$onMouseUp	, false );
		this._container.removeEventListener( 'mousedown'	, this._$onMouseDown	, false );
		this._container.removeEventListener( 'mousemove'	, this._$onMouseMove	, false );
	}
}

/**
 * @returns {Boolean} true if touchscreen is currently available, false otherwise
*/
VirtualJoystick.touchScreenAvailable	= function()
{
	return 'createTouch' in document ? true : false;
}

//////////////////////////////////////////////////////////////////////////////////
//										//
//////////////////////////////////////////////////////////////////////////////////

//VirtualJoystick.prototype.absX = function () { return this._stickX; }
//VirtualJoystick.prototype.absY = function () { return this._stickY; }

//VirtualJoystick.prototype.deltaX	= function(){ return this._stickX - this._baseX; }
//VirtualJoystick.prototype.deltaY	= function(){ return this._stickY - this._baseY;	}

VirtualJoystick.prototype.deltaX	= function(){ return this._stickX; }
VirtualJoystick.prototype.deltaY	= function(){ return this._stickY; }

//VirtualJoystick.prototype.deltaXPercent = function () { return ((this._stickX - (this._container.width() / 2)) / (this._container.width() / 2)) * 100; }
//VirtualJoystick.prototype.deltaYPercent = function () { return -((this._stickY - (this._container.height() / 2)) / (this._container.height() / 2)) * 100; }

VirtualJoystick.prototype.up	= function(){
	if( this._pressed === false )	return false;
	var deltaX	= this.deltaX();
	var deltaY	= this.deltaY();
	if( deltaY >= 0 )	return false;
	if( Math.abs(deltaY) < this._range && Math.abs(deltaY) < Math.abs(deltaX) ){
		return false;
	}
	return true;
}
VirtualJoystick.prototype.down	= function(){
	if( this._pressed === false )	return false;
	var deltaX	= this.deltaX();
	var deltaY	= this.deltaY();
	if( deltaY <= 0 )	return false;
	if( Math.abs(deltaY) < this._range && Math.abs(deltaY) < Math.abs(deltaX) ){
		return false;
	}
	return true;	
}
VirtualJoystick.prototype.right	= function(){
	if( this._pressed === false )	return false;
	var deltaX	= this.deltaX();
	var deltaY	= this.deltaY();
	if( deltaX <= 0 )	return false;
	if( Math.abs(deltaX) < this._range && Math.abs(deltaY) > Math.abs(deltaX) ){
		return false;
	}
	return true;	
}
VirtualJoystick.prototype.left	= function(){
	if( this._pressed === false )	return false;
	var deltaX	= this.deltaX();
	var deltaY	= this.deltaY();
	if( deltaX >= 0 )	return false;
	if( Math.abs(deltaX) < this._range && Math.abs(deltaY) > Math.abs(deltaX) ){
		return false;
	}
	return true;	
}

//////////////////////////////////////////////////////////////////////////////////
//										//
//////////////////////////////////////////////////////////////////////////////////

VirtualJoystick.prototype._onUp	= function()
{
	this._pressed	= false; 
	this._stickEl.style.display	= "none";
	//this._baseEl.style.display	= "none";
	
	//this._baseX	= this._baseY	= 0;
	this._stickX	= this._stickY	= 0;
}

VirtualJoystick.prototype._onDown	= function(x, y)
{
	this._pressed	= true; 
//	this._baseX	= x;
//	this._baseY	= y;
	this._stickX	= x - 200;
	this._stickY	= y - 200;

	this._stickEl.style.display	= "";
	this._stickEl.style.left	= (this._stickX - this._stickEl.width /2)+"px";
	this._stickEl.style.top		= (this._stickY - this._stickEl.height/2)+"px";

//	this._baseEl.style.display	= "";
//	this._baseEl.style.left		= (x - this._baseEl.width /2)+"px";
//	this._baseEl.style.top		= (y - this._baseEl.height/2)+"px";
}

VirtualJoystick.prototype._onMove	= function(x, y)
{
	if( this._pressed === true ){
		this._stickX	= x - 200;
		this._stickY	= y - 200;
		this._stickEl.style.left	= (this._stickX - this._stickEl.width /2)+"px";
		this._stickEl.style.top		= (this._stickY - this._stickEl.height/2)+"px";

//        this._stickEl.style.position = "absolute";
//        this._stickEl.style.left	= x+"px";
//        this._stickEl.style.top		= y+"px";
//        console.log("setting to " + this._stickEl.style.left + ":" + this._stickEl.style.top);
	}
}


//////////////////////////////////////////////////////////////////////////////////
//		bind touch events (and mouse events for debug)			//
//////////////////////////////////////////////////////////////////////////////////

VirtualJoystick.prototype._onMouseUp	= function(event)
{
	return this._onUp();
}

VirtualJoystick.prototype._onMouseDown	= function(event)
{
//	var x	= event.clientX - this._container.offsetLeft;
//	var y	= event.clientY - this._container.offsetTop;
    var x = event.offsetX;
    var y = event.offsetY;
//	var x	= event.clientX;
//	var y	= event.clientY;
	return this._onDown(x, y);
}

VirtualJoystick.prototype._onMouseMove	= function(event)
{
//	var x	= event.clientX - this._container.offsetLeft;
//	var y	= event.clientY - this._container.offsetTop;
    var x = event.offsetX;
    var y = event.offsetY;
//    var x	= event.clientX;
//    var y	= event.clientY;
//    console.log(x + ":" + y)
	return this._onMove(x, y);
}

VirtualJoystick.prototype._onTouchStart	= function(event)
{
	if( event.touches.length != 1 )	return;

	event.preventDefault();

	var x	= event.touches[ 0 ].pageX;
	var y	= event.touches[ 0 ].pageY;
	return this._onDown(x, y)
}

VirtualJoystick.prototype._onTouchEnd	= function(event)
{
//??????
// no preventDefault to get click event on ios
event.preventDefault();

	return this._onUp()
}

VirtualJoystick.prototype._onTouchMove	= function(event)
{
	if( event.touches.length != 1 )	return;

	event.preventDefault();

	var x	= event.touches[ 0 ].pageX;
	var y	= event.touches[ 0 ].pageY;
	return this._onMove(x, y)
}


//////////////////////////////////////////////////////////////////////////////////
//		build default stickEl and baseEl				//
//////////////////////////////////////////////////////////////////////////////////

VirtualJoystick.prototype._buildJoystickBase = function () {
    var canvas = document.createElement('canvas');
        canvas.width = 400;
        canvas.height = 400;
//    canvas.width = $("#container").width();
//    canvas.height = $("#container").height();
//    canvas.width = this._container.width;
//    canvas.height = this._container.height;

    var ctx = canvas.getContext('2d');
    ctx.beginPath();
    ctx.strokeStyle = "green";
    ctx.lineWidth = 6;
    ctx.arc(canvas.width / 2, canvas.height / 2, 40, 0, Math.PI * 2, true);
    ctx.stroke();

    ctx.beginPath();
    ctx.strokeStyle = "cyan";
    ctx.lineWidth = 2;
    ctx.arc(canvas.width / 2, canvas.height / 2, 60, 0, Math.PI * 2, true);
    ctx.stroke();

    this._maxSpeedRadius = canvas.width / 2;
    if (canvas.height < canvas.width) {
        this._maxSpeedRadius = canvas.height / 2;
    }
    ctx.beginPath();
    ctx.strokeStyle = "black";
    ctx.lineWidth = 2;
    ctx.arc(canvas.width / 2, canvas.height / 2, this._maxSpeedRadius, 0, Math.PI * 2, true);
    ctx.stroke();

    return canvas;
}

VirtualJoystick.prototype._buildJoystickStick	= function()
{
	var canvas	= document.createElement( 'canvas' );
	canvas.width	= 86;
	canvas.height	= 86;
	var ctx		= canvas.getContext('2d');
	ctx.beginPath(); 
	ctx.strokeStyle	= "cyan"; 
	ctx.lineWidth	= 6; 
	ctx.arc( canvas.width/2, canvas.width/2, 40, 0, Math.PI*2, true); 
	ctx.stroke();
	return canvas;
}

VirtualJoystick.prototype._buildJoystickButton	= function()
{
	var canvas	= document.createElement( 'canvas' );
	canvas.width	= 86;
	canvas.height	= 86;
	var ctx		= canvas.getContext('2d');
	ctx.beginPath(); 
	ctx.strokeStyle	= "red"; 
	ctx.lineWidth	= 6; 
	ctx.arc( canvas.width/2, canvas.width/2, 40, 0, Math.PI*2, true); 
	ctx.stroke();
	return canvas;
}

VirtualJoystick.prototype.getLeftSpeedPercentCommand = function () {

    if (!this._pressed) { return null; }

    // If you rotate point (px, py) around point (ox, oy) by angle theta you'll get:
    //
    // p'x = cos(theta) * (px-ox) - sin(theta) * (py-oy) + ox
    // p'y = sin(theta) * (px-ox) + cos(theta) * (py-oy) + oy

    var theta = -Math.PI / 4;
    var rotX = ((Math.cos(theta) * this.deltaX()) - (Math.sin(theta) * -this.deltaY())) * Math.SQRT2;

    if (rotX >= 0) {
        return Math.min((rotX / this._maxSpeedRadius) * 100, 100);
    } else {
        return Math.max((rotX / this._maxSpeedRadius) * 100, -100);
    }
}

VirtualJoystick.prototype.getRightSpeedPercentCommand = function () {
    if (!this._pressed) { return null; }

    var theta = -Math.PI / 4;
    //var rotX = ((Math.cos(theta) * this.deltaX()) - (Math.sin(theta) * -this.deltaY())) * Math.SQRT2;
    var rotY = ((Math.sin(theta) * this.deltaX()) + (Math.cos(theta) * -this.deltaY())) * Math.SQRT2;

    if (rotY >= 0) {
        return Math.min((rotY / this._maxSpeedRadius) * 100, 100);
    } else {
        return Math.max((rotY / this._maxSpeedRadius) * 100, -100);
    }
}

VirtualJoystick.prototype.getTouchRadians = function () {
    var x = this.deltaX();
    var y = -this.deltaY();
    var theta = Math.atan2(y, x);

    return theta;
}

VirtualJoystick.prototype.getTouchAngle = function () {
    return this.getTouchRadians() * (180 / Math.PI);
}

// rotate 45 degrees clockwise to get left side power
// rotate 45 degrees counter-clockwise to get right side power
// divide 

// If you rotate point (px, py) around point (ox, oy) by angle theta you'll get:
//
// p'x = cos(theta) * (px-ox) - sin(theta) * (py-oy) + ox
// p'y = sin(theta) * (px-ox) + cos(theta) * (py-oy) + oy