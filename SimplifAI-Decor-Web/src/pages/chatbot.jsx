import React from 'react';

function PageWithBackgroundImage() {
  return (
    <div style={{
      backgroundImage: 'url(https://drive.google.com/file/d/1r_tL4kVXBfmzZXxtTWDYd0fdKFx4ASfC/view?usp=sharing)', // Replace with your image path
      backgroundPosition: 'center',
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
      height: '100vh',
      width: '100vw',
    }}>
      </div>

  );
}

export default PageWithBackgroundImage;
