var DrawingArea = function(elementId) {
    this.canvas = document.getElementById(elementId);
    this.context = this.canvas.getContext("2d");
    this.penDown = false;
    this.lineStarted = false;
    this.touchMode = !!(navigator.userAgent.toLowerCase().match(/(android|iphone|ipod|ipad|blackberry)/));
    ...
}