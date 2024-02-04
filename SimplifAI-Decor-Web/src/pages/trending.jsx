import React from 'react';

import Card from './Card.jsx';

function Trending() {
    return (
        <div style={styles.pin_container}>
            <Card size="small" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/66/3e/53/663e53afd178901af689a5b59cbeeb51.jpg)`,
            }}/>
            <Card size="medium"style={{
                backgroundImage: `url(https://i.pinimg.com/236x/7e/c4/a2/7ec4a22085c3d5e8a3f7d9adc99fa879.jpg)`,
            }} />
            <Card size="large"style={{
                backgroundImage: `url(https://i.pinimg.com/236x/d8/b7/fb/d8b7fb89f0ea914925744f7cb766f526.jpg)`,
            }} />
            <Card size="small"style={{
                backgroundImage: `url(https://i.pinimg.com/236x/22/36/e2/2236e206ea7444e867d595f30c5240f7.jpg)`,
            }} />
            <Card size="medium" style={{
                backgroundImage: `url(https://i.pinimg.com/474x/11/e0/9b/11e09b5100d68a73ee6cb3484d5e8541.jpg)`,
            }}/>
            <Card size="large" style={{
                backgroundImage: `url(https://i.pinimg.com/474x/6e/1c/f2/6e1cf2f7927beb54701063c9b8e1cec2.jpg)`,
            }}/>
            <Card size="small" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/97/0b/05/970b053b6fb9b39ad1f21f24893d9664.jpg)`,
            }}/>
            <Card size="medium"style={{
                backgroundImage: `url(https://i.pinimg.com/564x/14/5e/fc/145efc03d7f19c6673dd1d005c41ab01.jpg)`,
            }} />
            <Card size="large" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/56/95/d7/5695d7338d8c5e2eba2ffa3147250ca2.jpg)`,
            }}/>
             <Card size="small"style={{
                backgroundImage: `url(https://i.pinimg.com/236x/22/36/e2/2236e206ea7444e867d595f30c5240f7.jpg)`,
            }} />
            <Card size="medium" style={{
                backgroundImage: `url(https://i.pinimg.com/474x/11/e0/9b/11e09b5100d68a73ee6cb3484d5e8541.jpg)`,
            }}/>
            <Card size="large" style={{
                backgroundImage: `url(https://i.pinimg.com/474x/6e/1c/f2/6e1cf2f7927beb54701063c9b8e1cec2.jpg)`,
            }}/>
            <Card size="small" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/97/0b/05/970b053b6fb9b39ad1f21f24893d9664.jpg)`,
            }}/>
            <Card size="medium"style={{
                backgroundImage: `url(https://i.pinimg.com/564x/14/5e/fc/145efc03d7f19c6673dd1d005c41ab01.jpg)`,
            }} />
            <Card size="large" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/56/95/d7/5695d7338d8c5e2eba2ffa3147250ca2.jpg)`,
            }}/>
             <Card size="small"style={{
                backgroundImage: `url(https://i.pinimg.com/236x/22/36/e2/2236e206ea7444e867d595f30c5240f7.jpg)`,
            }} />
            <Card size="medium" style={{
                backgroundImage: `url(https://i.pinimg.com/474x/11/e0/9b/11e09b5100d68a73ee6cb3484d5e8541.jpg)`,
            }}/>
            <Card size="large" style={{
                backgroundImage: `url(https://i.pinimg.com/474x/6e/1c/f2/6e1cf2f7927beb54701063c9b8e1cec2.jpg)`,
            }}/>
            <Card size="small" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/97/0b/05/970b053b6fb9b39ad1f21f24893d9664.jpg)`,
            }}/>
            <Card size="medium"style={{
                backgroundImage: `url(https://i.pinimg.com/564x/14/5e/fc/145efc03d7f19c6673dd1d005c41ab01.jpg)`,
            }} />
            <Card size="large" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/56/95/d7/5695d7338d8c5e2eba2ffa3147250ca2.jpg)`,
            }}/>
             <Card size="small"style={{
                backgroundImage: `url(https://i.pinimg.com/236x/22/36/e2/2236e206ea7444e867d595f30c5240f7.jpg)`,
            }} />
            <Card size="medium" style={{
                backgroundImage: `url(https://i.pinimg.com/474x/11/e0/9b/11e09b5100d68a73ee6cb3484d5e8541.jpg)`,
            }}/>
            <Card size="large" style={{
                backgroundImage: `url(https://i.pinimg.com/474x/6e/1c/f2/6e1cf2f7927beb54701063c9b8e1cec2.jpg)`,
            }}/>
            <Card size="small" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/97/0b/05/970b053b6fb9b39ad1f21f24893d9664.jpg)`,
            }}/>
            <Card size="medium"style={{
                backgroundImage: `url(https://i.pinimg.com/564x/14/5e/fc/145efc03d7f19c6673dd1d005c41ab01.jpg)`,
            }} />
            <Card size="large" style={{
                backgroundImage: `url(https://i.pinimg.com/236x/56/95/d7/5695d7338d8c5e2eba2ffa3147250ca2.jpg)`,
            }}/>
        </div>
    )
}

const styles = {
    pin_container: {
        //margin: '60px 0 0 0', // Adjust the top margin to 50px below the existing navbar
        paddingTop: '80px',
        width: 'calc(100vw - 100px)', // Adjusted width to fill up the desktop
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', // Adjusted gridTemplateColumns
        gridAutoRows: '10px',
        // position: 'absolute',
        left: 0,
        right: 0,
        // margin: '0 auto', // Center the container
        justifyContent: 'center',
    }
}

export default Trending;