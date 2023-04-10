function Carousel() {
    return (
        <div id="pineapple_carousel" class="carousel slide" data-bs-ride="true">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#pineapple_carousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#pineapple_carousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#pineapple_carousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="PropertyData/Pineapple1.jpg" class="d-block w-100" alt="..."></img>
            </div>
            <div class="carousel-item">
              <img src="PropertyData/Pineapple2.jpg" class="d-block w-100" alt="..."></img>
            </div>
            <div class="carousel-item">
              <img src="PropertyData/Pineapple3.jpg" class="d-block w-100" alt="..."></img>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#pineapple_carousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#pineapple_carousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
    );
  }
  
  export default Carousel;
  