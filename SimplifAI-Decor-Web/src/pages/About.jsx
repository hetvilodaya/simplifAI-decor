import React from "react";
import hetviImage from "../assets/images/hetvi.jpg";
import renaImage from "../assets/images/rena.jpeg";
import malharImage from "../assets/images/malhar.jpeg";
import nishthaImage from "../assets/images/nishtha.jpg";

const teamMembers = [
  { name: "Hetvi Lodaya", role: "Frontend Developer", imgSrc: hetviImage },
  { name: "Rena Shah", role: "AI/ML Developer", imgSrc: renaImage },
  { name: "Malhar Bonde", role: "Backend Developer", imgSrc: malharImage },
  { name: "Nishtha Chitalia", role: "App Developer", imgSrc: nishthaImage },
];

const TeamSection = () => {
  return (
    <section style={{ background: "#f5f5f5" }}>
      <div style={{ display: "flex", flexWrap: "wrap", padding: "2em 1em", textAlign: "center" }}>
        <h1 style={{ paddingTop: "10%", width: "100%", textAlign: "center", fontSize: "3.5em", color: "#1f003b" }}>Our Team</h1>
      </div>
      <div style={{ paddingLeft: "8%", display: "flex", flexWrap: "wrap", paddingBottom: "8%" }}>
        {teamMembers.map((member, index) => (
          <div key={index} style={{ flexBasis: 0, flexGrow: 1, padding: "0.5em 0" }}>
            <div style={{ paddingLeft: "8%", width: "80%", boxShadow: "0 0 2.4em rgba(25, 0, 58, 0.1)", padding: "3.5em 1em", borderRadius: "0.6em", color: "#1f003b", cursor: "pointer", transition: "0.3s", backgroundColor: "#ffffff" }}>
              <div style={{ width: "8em", height: "8em", backgroundColor: "#a993ff", padding: "0.5em", borderRadius: "50%", margin: "0 auto 2em auto" }}>
                <img style={{ width: "100%", height: "100%",objectFit:'cover', borderRadius: "50%" }} src={member.imgSrc} alt={`${member.name}Image`} />
              </div>
              <h3 style={{ fontWeight: 500 }}>{member.name}</h3>
              <p style={{ fontWeight: 300, textTransform: "uppercase", margin: "0.5em 0 2em 0", letterSpacing: "2px" }}>{member.role}</p>
              <div style={{ width: "50%", minWidth: "180px", margin: "auto", display: "flex", justifyContent: "space-between" }}>
                <a href="#" style={{ textDecoration: "none", color: "inherit", fontSize: "1.4em" }}>
                  <i className="fab fa-twitter"></i>
                </a>
                <a href="#" style={{ textDecoration: "none", color: "inherit", fontSize: "1.4em" }}>
                  <i className="fab fa-linkedin"></i>
                </a>
                <a href="#" style={{ textDecoration: "none", color: "inherit", fontSize: "1.4em" }}>
                  <i className="fab fa-github"></i>
                </a>
                <a href="#" style={{ textDecoration: "none", color: "inherit", fontSize: "1.4em" }}>
                  <i className="fas fa-envelope"></i>
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default TeamSection;
