import React from "react";

const Footer = () => {
  return (
    <div>
      <section className="footer">
        <div className="container">
          <div className="row">
            <div className="col-lg-6">
              <div className="contact-info">
                <h4 style={{ color: "white" }}>Contact Info</h4>
                <p style={{ color: "white" }}>
                  CR 34, CSE(ICB),<br />
                  Dwarkadas J. Sanghvi College of Engineering <br />
                  2hlodaya@gmail.com <br />
                  +91 9619318431
                </p>
              </div>
            </div>
            <div className="col-lg-6">
              <div className="widget footer-widget text-lg-right mt-5 mt-lg-0"></div>
            </div>
          </div>
          <div className="row">
            <div className="col-lg-6">
              <p style={{ color: "white" }} className="mb-0">
                Designed & Developed by&nbsp;&nbsp;mkdir team_name
              </p>
            </div>
            <div className="col-lg-6">
              <div className="widget footer-widget text-lg-right mt-5 mt-lg-0"></div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Footer;
