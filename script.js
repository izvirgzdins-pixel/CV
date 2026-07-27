const projects = [
  {
    id: "bubblebee",
    title: "Microphone Handling-Noise Reduction",
    company: "Bubblebee Industries",
    year: "2025.03 - 2026.07",
    category: "engineering",
    featured: true,
    tags: ["Engineering", "Audio hardware", "Quick release", "Vibration analysis", "ESP32"],
    image: "assets/bbi-blimp-render-dark.jpg",
    gallery: [
      "assets/bbi-blimp-render-dark.jpg",
      "assets/bbi-quickrelease-render-dark.jpg",
      "assets/bbi-shockmount-render-dark.jpg",
      "assets/bbi-blimp-cad.png",
      "assets/bbi-quickrelease-part.png",
      "assets/bbi-connector-assembly.png",
      "assets/bbi-connector-side.png",
      "assets/bbi-microphone-cad.png",
      "assets/bbi-transmittance-chart.png",
      "assets/bbi-technical-drawing.png",
      "assets/bbi-eccentric-clamp-drawing.png",
    ],
    summary:
      "Audio-recording microphone handling-noise reduction equipment, quick-release mechanism design for microphone blimps, and vibration validation tooling.",
    bullets: [
      "Designed quick-release mechanism concepts for microphone blimp hardware.",
      "Developed and validated handling-noise reduction equipment for audio recording workflows.",
      "Built a validation test-stand approach using ESP32, Codex-assisted jig development, data logging, and acceleration measurements.",
      "Used transmittance and vibration analysis to compare mechanical configurations and guide design iteration.",
    ],
  },
  {
    id: "warp-lustra",
    title: "2 x 7 m Kinematic Robotic Chandelier",
    company: "Warp Agency",
    year: "2023.06 - 2023.08",
    category: "engineering",
    featured: true,
    tags: ["Engineering", "Kinematics", "Robotics", "Installation", "CAD"],
    image: "assets/warp-lustra-installed-overview.jpg",
    gallery: [
      "assets/warp-lustra-installed-overview.jpg",
      "assets/warp-lustra-installed-open.jpg",
      "assets/warp-lustra-installed-diagonal.jpg",
      "assets/warp-lustra-room-context.jpg",
      "assets/warp-lustra-parts-array.jpg",
      "assets/warp-lustra-carriage-detail.jpg",
      {
        type: "video",
        src: "assets/warp-lustra-motion-0591.mp4",
      },
      {
        type: "video",
        src: "assets/warp-lustra-motion-0598.mp4",
      },
      {
        type: "video",
        src: "assets/warp-lustra-motion-0593.mp4",
      },
      {
        type: "video",
        src: "assets/warp-lustra-motion-0590.mp4",
      },
    ],
    summary:
      "Mechanical design and prototyping for a 2 x 7 m kinematic robotic chandelier for Gravity Team/Lustra, focused on quiet, robust motion.",
    bullets: [
      "Created the mechanical architecture for a large-format kinetic lighting installation.",
      "Designed rail, pulley, actuator, and support details for reliable low-noise movement.",
      "Built and validated workshop prototypes before ceiling installation.",
      "Prepared SolidWorks assemblies, part models, and installation-ready mechanical details.",
    ],
  },
  {
    id: "giraffe360",
    title: "Lidar Motor & Optical Tooling",
    company: "Giraffe360",
    year: "2023 - 2025",
    category: "engineering",
    tags: ["Engineering", "Validation", "Tooling", "Prototyping"],
    image: "assets/giraffe360-lidar-optics-assembly-enhanced.jpg",
    gallery: [
      "assets/giraffe360-lidar-optics-assembly-enhanced.jpg",
      "assets/giraffe360-lidar-motor-assembly-enhanced.jpg",
      "assets/giraffe360-cad-section-enhanced.jpg",
      "assets/giraffe360-cad-transparent-housing-enhanced.jpg",
      "assets/giraffe360-cad-lens-bracket-enhanced.jpg",
      "assets/giraffe360-cad-rotor-assembly-enhanced.jpg",
      "assets/giraffe360-cad-optical-tooling-enhanced.jpg",
      "assets/giraffe360-cad-needle-applicator-enhanced.jpg",
      "assets/giraffe360-cad-adjustment-frame-enhanced.jpg",
      "assets/giraffe360-cad-clamp-detail-enhanced.jpg",
      {
        type: "video",
        src: "assets/giraffe360-lidar-motion-1001.mp4",
        poster: "assets/giraffe360-lidar-optics-assembly-enhanced.jpg",
      },
      {
        type: "video",
        src: "assets/giraffe360-lidar-motion-1795.mp4",
        poster: "assets/giraffe360-lidar-motor-assembly-enhanced.jpg",
      },
    ],
    summary:
      "Lidar-integrated brushless motor R&D, optical component alignment, prototype validation, and assembly process tooling.",
    links: [
      {
        label: "Giraffe360 website",
        href: "https://www.giraffe360.com/",
      },
    ],
    bullets: [
      "Injection-moulded part design and supplier communication.",
      "CFD and real-world validation across FDM, SLA, SLS, and CNC prototypes.",
      "Optical component glueing robot and adjustment frame development.",
      "PCB testing jigs and assembly issue evaluation.",
    ],
  },
  {
    id: "rtu-load-cell",
    title: "Scaffolding Pressure Sensor",
    company: "Riga Technical University",
    year: "2022 - 2023",
    category: "engineering",
    tags: ["Engineering", "IP68", "FEA", "Wireless"],
    image: "assets/rtu-scaffolding-sensor-ipin.jpg",
    gallery: [
      "assets/img-008.png",
      "assets/img-009.png",
      "assets/img-010.png",
      "assets/rtu-scaffolding-sensor-ipin.jpg",
    ],
    summary:
      "Load-cell based scaffolding pressure sensor with sealed mechanical architecture and wireless operation.",
    bullets: [
      "Overmoulded PU rubber, LoRa antenna, and wireless charging integration.",
      "Sheet metal laser-cut covers and PCB mechanical layout.",
      "Battery block assembly and FEA stress analysis.",
      "IP68-rated mechanical design.",
    ],
  },
  {
    id: "upcatalyst",
    title: "Carbon Scraper Mechanism",
    company: "UpCatalyst",
    year: "2023",
    category: "engineering",
    tags: ["Mechanisms", "FEA", "Industrial process"],
    image: "assets/img-013.png",
    gallery: [
      "assets/img-013.png",
      "assets/upcatalyst-scraper-container-clean.jpg",
      "assets/img-012.png",
      "assets/upcatalyst-container-overview.jpg",
      "assets/upcatalyst-process-interior.jpg",
      "assets/upcatalyst-control-workstation.jpg",
    ],
    summary:
      "Mechanical scraper concept, layout, calculations, and technical documentation for an industrial process mechanism.",
    links: [
      {
        label: "UpCatalyst website",
        href: "https://upcatalyst.com/",
      },
    ],
    bullets: [
      "Scraper design and technical layout.",
      "Mechanical calculations for expected loads.",
      "FEA stress analysis.",
      "Technical drawings for parts and assembly.",
    ],
  },
  {
    id: "spectrum-compact",
    title: "Spectrum Compact Product Group",
    company: "SAFtehnika JSC",
    year: "2015 - 2022",
    category: "industrial-design",
    tags: ["Industrial design", "RF equipment", "IP54", "DFM"],
    image: "assets/img-017.png",
    gallery: ["assets/img-014.png", "assets/img-015.png", "assets/img-016.png", "assets/img-017.png"],
    summary:
      "Mechanical and industrial design for a 0.3-80 GHz radio spectrum analyser used by installers and regulatory institutions.",
    links: [
      {
        label: "Spectrum Compact website",
        href: "http://www.spectrumcompact.com/",
      },
    ],
    bullets: [
      "CNC milling, CNC turning, sheet metal, and silicone moulding details.",
      "PCB layout support, engineering drawings, and assembly drawings.",
      "IP54 solution and documentation drawings.",
      "Product group ownership from concept to manufacturable detail.",
    ],
  },
  {
    id: "spectrum-drone",
    title: "Spectrum Compact Drone Modification",
    company: "SAFtehnika JSC / LMT",
    year: "2015 - 2022",
    category: "engineering",
    tags: ["Engineering", "Drone attachment", "RF monitoring", "Vibration damping"],
    image: "assets/img-018.png",
    gallery: ["assets/img-018.png", "assets/img-019.png"],
    summary:
      "Drone-mounted Spectrum Compact modification for on-site RF tower monitoring and audit work, developed in collaboration with Latvijas Mobilais Telefons (LMT).",
    links: [
      {
        label: "Promotion video",
        href: "https://www.youtube.com/watch?v=2vpvI6SakXY",
      },
      {
        label: "Drone-based AI article",
        href: "https://spectrumcompact.com/drone-based-ai-solution-for-rf-tower-monitoring-and-audit/",
      },
    ],
    bullets: [
      "Modular lightweight attachment concept for drone-based regulatory work.",
      "IR camera implementation support for dedicated software workflows.",
      "Vibration damping solution for airborne measurement hardware.",
      "Easy-to-exchange RF polarization and mechanical component assembly.",
      "Manufacturing drawings, 3D printing, and prototyping.",
    ],
  },
  {
    id: "integra-e2",
    title: "Integra-E2 5G Radio Equipment",
    company: "SAFtehnika JSC",
    year: "2015 - 2022",
    category: "engineering",
    tags: ["Engineering", "5G radio", "Radio antenna", "IP68", "ATEX"],
    image: "assets/integra-e2-render-angle.png",
    gallery: [
      "assets/integra-e2-render-angle.png",
      "assets/integra-e2-render-rear.png",
      "assets/integra-e2-render-front.png",
    ],
    summary:
      "Lead mechanical engineering for point-to-point 5G radio equipment with a simple, robust enclosure philosophy.",
    links: [
      {
        label: "Integra-E product page",
        href: "http://saftehnika.com/en/integrae",
      },
    ],
    bullets: [
      "Aluminium extruded base and CNC milled aluminium heatsink cover.",
      "IP68-rated design and ATEX certification support.",
      "Engineering drawings, assembly drawings, and BOM.",
      "Mechanical solution aligned with company product design guidelines.",
    ],
  },
  {
    id: "aranet",
    title: "Aranet IoT Sensor Family",
    company: "SAFtehnika JSC / Aranet",
    year: "2015 - 2022",
    category: "industrial-design",
    tags: ["Industrial design", "IoT", "Injection moulding", "Mass production"],
    image: "assets/img-023.png",
    gallery: ["assets/img-023.png", "assets/img-024.png", "assets/img-025.png", "assets/img-026.png", "assets/img-027.png", "assets/img-028.png"],
    summary:
      "Industrial design and engineering for LoRa sensor products used in farming, horticulture, offices, and education.",
    links: [
      {
        label: "Aranet website",
        href: "https://aranet.com/",
      },
      {
        label: "Aranet shop",
        href: "https://shop.aranet.com/europe/all",
      },
    ],
    bullets: [
      "Plastic injection-moulded part design and engineering.",
      "IP68-rated sensor design, engineering drawings, assembly drawings, quality control, and BOM.",
      "Aranet4 CO2 sensor reached more than 100,000 produced units.",
      "Aranet4 awarded Latvia's Most Innovative Product of 2019.",
    ],
  },
  {
    id: "chemical-gas",
    title: "Chemical Gas Sensor",
    company: "Aranet",
    year: "2015 - 2022",
    category: "prototyping",
    tags: ["Prototyping", "IP68", "Airtight assembly"],
    image: "assets/img-029.png",
    gallery: ["assets/img-029.png", "assets/img-030.png", "assets/img-031.png"],
    summary:
      "IP68 gas sensor concept with an airtight assembly approach and simplified mechanical construction.",
    bullets: [
      "Simple airtight assembly without screws.",
      "Compact internal layout and enclosure detail design.",
      "Product visualization for design evaluation.",
    ],
  },
  {
    id: "fire-alarm",
    title: "Fire Alarm Security System",
    company: "SAFtehnika JSC",
    year: "2015 - 2022",
    category: "industrial-design",
    tags: ["Industrial design", "EN-54", "Safety devices"],
    image: "assets/img-032.png",
    gallery: [
      "assets/img-032.png",
      "assets/fire-alarm-smoke-detector-render.png",
      "assets/fire-alarm-sounder-strobe-render.png",
      "assets/fire-alarm-red-detector-render.png",
    ],
    summary:
      "Design development for a fire alarm product group in accordance with EN-54 requirements.",
    bullets: [
      "Base station, smoke detector, and sound/light alarm design.",
      "Multiple product render directions for review and selection.",
      "Mechanical form exploration for wall and ceiling-mounted devices.",
    ],
  },
  {
    id: "technical-drawings",
    title: "Production Drawings",
    company: "Technical documentation",
    year: "Ongoing",
    category: "documentation",
    tags: ["Documentation", "Drawings", "Manufacturing"],
    image: "assets/img-040.png",
    gallery: ["assets/img-040.png", "assets/img-041.png", "assets/img-042.png", "assets/img-043.png"],
    summary:
      "Assembly and production-ready technical drawing packages for mechanical parts and product structures.",
    bullets: [
      "Exploded views, part details, and assembly layouts.",
      "Manufacturing drawings for supplier communication.",
      "Documentation support for production and quality control.",
    ],
  },
  {
    id: "et-sons",
    title: "Latvian Architecture Award Object",
    company: "ET Sons",
    year: "2015",
    category: "industrial-design",
    tags: ["Industrial design", "Award object", "5-axis CNC"],
    image: "assets/img-044.png",
    gallery: ["assets/img-044.png", "assets/img-045.png"],
    summary:
      "Rubik's cube pineapple award object with 50+ parts, produced using 5-axis CNC milling.",
    bullets: [
      "Industrial design and project management.",
      "Complex multi-part assembly with precision manufacturing.",
      "Visual design by A. Analts and R. Strelis.",
    ],
  },
  {
    id: "mood-am",
    title: "Magnetic Watch Strap System",
    company: "MOOD AM",
    year: "2015",
    category: "prototyping",
    tags: ["Prototyping", "Wearable hardware", "Magnetic concept"],
    image: "assets/img-046.png",
    gallery: ["assets/img-046.png", "assets/img-047.png"],
    summary:
      "Watch concept with easily replaceable magnetic straps and a clean, minimal product language.",
    bullets: [
      "Magnetic strap replacement concept.",
      "Simple industrial design direction.",
      "Prototype-ready visualization for client review.",
    ],
  },
];

const grid = document.querySelector("#projectGrid");
const modal = document.querySelector("#projectModal");
const modalPanel = document.querySelector(".modal-panel");
const modalImage = document.querySelector("#modalImage");
const modalVideo = document.querySelector("#modalVideo");
const modalCompany = document.querySelector("#modalCompany");
const modalTitle = document.querySelector("#modalTitle");
const modalDescription = document.querySelector("#modalDescription");
const modalLinks = document.querySelector("#modalLinks");
const modalBullets = document.querySelector("#modalBullets");
const imageCounter = document.querySelector("#imageCounter");
const previousImage = document.querySelector("#previousImage");
const nextImage = document.querySelector("#nextImage");

let activeProject = null;
let activeImageIndex = 0;

function renderLinks(links = []) {
  return links
    .map(
      (link) => `
        <a href="${link.href}" target="_blank" rel="noreferrer">
          ${link.label}
        </a>
      `,
    )
    .join("");
}

function getGalleryItem(item) {
  return typeof item === "string" ? { type: "image", src: item } : item;
}

function getVideoType(src) {
  return src.toLowerCase().endsWith(".mov") ? "video/quicktime" : "video/mp4";
}

function renderProjects() {
  grid.innerHTML = projects
    .map(
      (project) => `
        <button
          class="project-card${project.featured ? " is-featured" : ""}"
          type="button"
          data-project-id="${project.id}"
          aria-expanded="false"
          aria-controls="projectModal"
        >
          <img src="${project.image}" alt="${project.title}" loading="lazy" decoding="async">
          <span class="project-card-content">
            <span class="project-meta">
              <span>${project.company}</span>
              <span>${project.year}</span>
            </span>
            <h3>${project.title}</h3>
            <p>${project.summary}</p>
            <span class="project-action">View media</span>
          </span>
        </button>
      `,
    )
    .join("");
}

function setProjectExpanded(projectId = null) {
  grid.querySelectorAll(".project-card[aria-expanded]").forEach((card) => {
    card.setAttribute("aria-expanded", card.dataset.projectId === projectId ? "true" : "false");
  });
}

function updateModalImage() {
  if (!activeProject) return;
  const currentItem = getGalleryItem(activeProject.gallery[activeImageIndex]);
  const label = `${activeProject.title} media ${activeImageIndex + 1}`;

  if (currentItem.type === "video") {
    modalImage.hidden = true;
    modalImage.removeAttribute("src");
    modalImage.alt = "";
    modalVideo.hidden = false;
    modalVideo.muted = true;
    modalVideo.preload = "auto";
    modalVideo.poster = currentItem.poster || "";
    modalVideo.innerHTML = `<source src="${currentItem.src}" type="${getVideoType(currentItem.src)}">`;
    modalVideo.setAttribute("aria-label", label);
    modalVideo.load();
  } else {
    modalVideo.pause();
    modalVideo.hidden = true;
    modalVideo.removeAttribute("poster");
    modalVideo.innerHTML = "";
    modalImage.hidden = false;
    modalImage.src = currentItem.src;
    modalImage.alt = label;
  }

  imageCounter.textContent = `${activeImageIndex + 1} / ${activeProject.gallery.length}`;
  requestAnimationFrame(() => {
    if (modalPanel) modalPanel.scrollTop = 0;
  });
}

function openProject(projectId) {
  activeProject = projects.find((project) => project.id === projectId);
  if (!activeProject) return;

  activeImageIndex = 0;
  modalCompany.textContent = activeProject.company;
  modalTitle.textContent = activeProject.title;
  modalDescription.textContent = activeProject.summary;
  modalLinks.innerHTML = renderLinks(activeProject.links);
  modalLinks.hidden = !activeProject.links || activeProject.links.length === 0;
  modalBullets.innerHTML = activeProject.bullets.map((item) => `<li>${item}</li>`).join("");
  updateModalImage();
  modal.classList.add("is-open");
  modal.setAttribute("aria-hidden", "false");
  setProjectExpanded(activeProject.id);
  document.body.style.overflow = "hidden";
}

function closeModal() {
  setProjectExpanded();
  modalVideo.pause();
  modal.classList.remove("is-open");
  modal.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
  activeProject = null;
}

grid.addEventListener("click", (event) => {
  const card = event.target.closest(".project-card");
  if (!card) return;
  openProject(card.dataset.projectId);
});

document.querySelectorAll("[data-close-modal]").forEach((button) => {
  button.addEventListener("click", closeModal);
});

previousImage.addEventListener("click", () => {
  if (!activeProject) return;
  activeImageIndex =
    (activeImageIndex - 1 + activeProject.gallery.length) % activeProject.gallery.length;
  updateModalImage();
});

nextImage.addEventListener("click", () => {
  if (!activeProject) return;
  activeImageIndex = (activeImageIndex + 1) % activeProject.gallery.length;
  updateModalImage();
});

document.addEventListener("keydown", (event) => {
  if (!modal.classList.contains("is-open")) return;

  if (event.key === "Escape") {
    closeModal();
  }

  if (event.key === "ArrowLeft") {
    previousImage.click();
  }

  if (event.key === "ArrowRight") {
    nextImage.click();
  }
});

renderProjects();

function alignHashTarget() {
  if (!location.hash) return;
  const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (!target) return;
  const anchor = target.querySelector(".section-heading") || target;
  const header = document.querySelector(".site-header");
  const headerOffset = header && getComputedStyle(header).position !== "static" ? header.offsetHeight : 0;
  const top = anchor.getBoundingClientRect().top + window.scrollY - headerOffset - 22;
  requestAnimationFrame(() => {
    window.scrollTo({ top: Math.max(0, top), behavior: "auto" });
  });
}

alignHashTarget();
window.addEventListener("hashchange", alignHashTarget);
window.addEventListener("load", () => {
  alignHashTarget();
  window.setTimeout(alignHashTarget, 250);
  window.setTimeout(alignHashTarget, 900);
});
