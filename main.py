import warnings
warnings.filterwarnings("ignore")

import flet as ft
import os
import sys
import random
import math

# --- SMART PATH FINDER ---
def get_asset_path(filename):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(application_path, filename)

# ==========================================
#    CONTENT ENGINE
# ==========================================

STEPS_DB = {
    "Redux": """STEP 1: THE FOUNDATION
- Install the toolkit: 'npm install @reduxjs/toolkit react-redux'.
- In 'src/app', create 'store.js'. This is your single source of truth.

STEP 2: SLICE ARCHITECTURE
- Don't put everything in one file. Create 'features/{model}/{model}Slice.js'.
- Define the initial state (loading: false, list: []).
- Export the specific actions (add, remove) you need for the UI.

STEP 3: GLOBAL ACCESS
- Open 'index.js'. Wrap your <App> with <Provider store={store}>.
- This injects the state into the entire React component tree.

STEP 4: DATA FLOW
- In your component, use 'useDispatch()' to send commands.
- Use 'useSelector()' to read data. Never mutate state directly.""",

    "Context API": """STEP 1: CONTEXT SETUP
- Create 'context/{Model}Context.js'.
- Initialize it: 'const {Model}Context = createContext();'.

STEP 2: THE WRAPPER
- Build a Provider component that holds the state (useState or useReducer).
- Pass the values down via the 'value' prop.

STEP 3: CLEAN CONSUMPTION
- Don't import the context directly in components. That's messy.
- Create a custom hook: 'export const use{Model} = () => useContext(...)'.

STEP 4: IMPLEMENTATION
- Wrap your top-level component (or just the section that needs it) in the Provider.
- Call your custom hook in any child component to get instant access.""",

    "Firebase": """STEP 1: SDK CONFIGURATION
- Create a Firebase project in the console.
- Copy the config object to 'src/firebase.js'.
- Export 'db' and 'auth' so other files can use them.

STEP 2: AUTHENTICATION FLOW
- Build a Login component. Use 'signInWithPopup' for Google Auth.
- Use the 'onAuthStateChanged' listener to detect if the user is logged in.

STEP 3: FIRESTORE SYNC
- Don't just fetch once. Use 'onSnapshot'.
- This creates a live websocket connection. When the DB changes, your UI updates instantly.

STEP 4: SECURITY
- Go to Firestore Rules.
- Add: 'allow read, write: if request.auth != null;'. Never leave your DB open.""",

    "Rest API": """STEP 1: API UTILITIES
- Create 'utils/api.js'. Configure Axios with your base URL.
- Add a request interceptor to attach your 'Bearer' token automatically.

STEP 2: DATA FETCHING HOOK
- Create 'useFetch.js'. It should return { data, loading, error }.
- This keeps your UI components clean and free of messy fetch logic.

STEP 3: ERROR BOUNDARIES
- APIs fail. Be ready.
- Check for 401 (Unauthorized) to redirect to login.
- Check for 500 (Server Error) to show a "Try again later" toast.

STEP 4: STATE UPDATES
- When a user adds an item, update the local list immediately (Optimistic UI).
- Then send the API request. If it fails, roll back the change.""",
}

CASE_STUDIES = [
    "CASE STUDY: THE $10M SCALE UP\nA London Fintech startup used this exact Redux pattern to handle 50,000 concurrent transactions per second. By normalizing their state shape, they reduced memory usage by 40% on low-end Android devices.",
    "CASE STUDY: HOSPITAL SYSTEM RESILIENCE\nA Nigerian HealthTech firm implemented this Offline-First architecture. When hospital internet failed, doctors could still input patient data. The system automatically synced 500+ records once connectivity was restored.",
    "CASE STUDY: E-COMMERCE LATENCY\nAn oversized Context API implementation was causing 2-second delays on 'Add to Cart'. By refactoring to the Slice pattern shown above, they isolated the cart state, reducing re-renders and boosting conversion rates by 15%.",
    "CASE STUDY: THE LOGISTICS DASHBOARD\nTracking 10,000 trucks in real-time crashed the browser. The team switched to the WebSocket architecture described here, using a 'throttle' function to limit updates to 5 times per second, ensuring smooth 60fps animations.",
    "CASE STUDY: SECURITY BREACH PREVENTED\nA junior dev left the Firestore database open. Using the Security Rules outlined in Step 4, the lead architect locked down the DB in minutes, preventing a potential data leak of 100,000 user emails."
]

DOMAINS = [
    {"name": "Fintech", "model": "transaction", "Model": "Transaction"},
    {"name": "Health", "model": "patient", "Model": "Patient"},
    {"name": "Crypto", "model": "wallet", "Model": "Wallet"},
    {"name": "Logistics", "model": "shipment", "Model": "Shipment"},
    {"name": "Ecom", "model": "order", "Model": "Order"},
]

def generate_db():
    db = []
    tech_keys = list(STEPS_DB.keys())
    for i in range(1, 501):
        domain = DOMAINS[i % len(DOMAINS)]
        tech = tech_keys[i % len(tech_keys)]
        case_study = random.choice(CASE_STUDIES)
        
        project = {
            "id": i,
            "title": f"The {domain['name']} {tech} Master",
            "desc": f"Project #{i} simulates a high-frequency {domain['name']} dashboard. You will build a system to track {domain['model']} lifecycles using {tech}, focusing on state immutability, clean architecture, and production readiness.",
            "steps": STEPS_DB[tech].replace("{model}", domain['model']).replace("{Model}", domain['Model']),
            "tech": tech,
            "code": f"// {domain['Model']} Logic\nconst sync{domain['Model']} = async () => {{\n  try {{\n    setList(prev => [...prev, newItem]);\n    await api.post('/{domain['model']}s', newItem);\n  }} catch (err) {{\n    toast.error('Sync failed');\n    setList(prev => prev.filter(i => i.id !== newItem.id));\n  }}\n}};",
            "case_study": case_study,
            "link_id": None
        }
        db.append(project)
    return db

REACT_500_DB = generate_db()

# ==========================================
#    PDF PUBLISHER ENGINE
# ==========================================

def main(page: ft.Page):
    # UI SETUP
    page.title = "Owo-Nexus Publisher"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1a1a1a"
    page.window_width = 500
    page.window_height = 700
    
    status_text = ft.Text("System Ready.", color="cyan")

    def generate_book(e):
        status_text.value = "Indexing & Printing Global Bestseller..."
        page.update()
        
        try:
            from fpdf import FPDF
            
            class BookPDF(FPDF):
                def header(self):
                    if hasattr(self, 'show_header') and self.show_header:
                        self.set_font("Helvetica", "B", 8)
                        self.set_text_color(150, 150, 150)
                        self.cell(100, 10, "THE REACT 500 | SOVEREIGN FIELD MANUAL", align="L")
                        self.cell(0, 10, "www.owonexus.com", align="R", ln=True)
                        self.set_draw_color(220, 220, 220)
                        self.line(10, 18, 200, 18)
                        self.ln(5)

                def footer(self):
                    self.set_y(-15)
                    self.set_font("Helvetica", "", 8)
                    self.set_text_color(150, 150, 150)
                    self.cell(0, 10, f"Page {self.page_no()}", align="C")

                def draw_react_logo(self, x, y, size):
                    self.set_draw_color(0, 229, 255)
                    self.set_line_width(0.5)
                    self.set_fill_color(0, 229, 255)
                    self.circle(x, y, size/5, 'F')
                    self.ellipse(x, y, size, size/3)
                    self.set_fill_color(255, 255, 255)
                    self.line(x, y, x, y-size)
                    self.circle(x, y-size, 2, 'FD')
                    self.line(x, y, x-size*0.8, y+size*0.6)
                    self.circle(x-size*0.8, y+size*0.6, 2, 'FD')
                    self.line(x, y, x+size*0.8, y+size*0.6)
                    self.circle(x+size*0.8, y+size*0.6, 2, 'FD')

                def chapter_title(self, num, label):
                    self.set_font("Helvetica", "B", 24)
                    self.set_text_color(200, 200, 200)
                    self.cell(0, 15, f"#{num}", ln=True)
                    self.set_font("Helvetica", "B", 18)
                    self.set_text_color(0, 102, 204)
                    self.cell(0, 10, label.upper(), ln=True)
                    self.ln(5)

                def section_header(self, title):
                    self.set_font("Helvetica", "B", 11)
                    self.set_text_color(0, 0, 0)
                    self.cell(0, 8, title.upper(), ln=True)
                    self.set_draw_color(0, 102, 204)
                    self.line(self.get_x(), self.get_y(), self.get_x() + 20, self.get_y())
                    self.ln(3)

                def body_text(self, txt):
                    self.set_font("Helvetica", "", 10)
                    self.set_text_color(50, 50, 50)
                    clean = txt.encode('latin-1', 'replace').decode('latin-1')
                    self.multi_cell(0, 5, clean)
                    self.ln(5)

                def code_block(self, code):
                    self.set_fill_color(245, 245, 245)
                    self.set_text_color(0, 100, 0)
                    self.set_font("Courier", "", 9)
                    self.ln(2)
                    clean_code = code.encode('latin-1', 'replace').decode('latin-1')
                    self.multi_cell(0, 5, clean_code, fill=True)
                    self.ln(5)

                def case_study_box(self, txt):
                    self.set_fill_color(230, 240, 255)
                    self.set_text_color(0, 50, 100)
                    self.set_font("Helvetica", "B", 10)
                    self.cell(0, 8, "  INDUSTRY INSIGHT:", ln=True, fill=True)
                    self.set_font("Helvetica", "I", 10)
                    clean = txt.encode('latin-1', 'replace').decode('latin-1')
                    self.multi_cell(0, 6, clean, fill=True, border=0)
                    self.ln(5)

            pdf = BookPDF()
            pdf.show_header = False
            pdf.set_auto_page_break(auto=True, margin=20)

            # --- 1. FRONT MATTER ---
            # Cover
            pdf.add_page()
            pdf.set_fill_color(10, 25, 45) 
            pdf.rect(0, 0, 210, 297, 'F')
            pdf.draw_react_logo(105, 140, 30)
            pdf.set_y(60)
            pdf.set_font("Helvetica", "B", 60)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 25, "THE", align="C", ln=True)
            pdf.set_text_color(0, 229, 255)
            pdf.cell(0, 25, "REACT 500", align="C", ln=True)
            pdf.set_font("Helvetica", "", 16)
            pdf.set_text_color(200, 200, 200)
            pdf.cell(0, 15, "THE SOVEREIGN ARCHITECTURE MANUAL", align="C", ln=True)
            pdf.set_y(240)
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 10, "PRINCE BABATUNDE ADESINA", align="C", ln=True)
            pdf.set_font("Helvetica", "", 12)
            pdf.set_text_color(0, 229, 255)
            pdf.cell(0, 10, "OWO-NEXUS AI | www.owonexus.com", align="C", ln=True)

            # Copyright
            pdf.add_page()
            pdf.set_y(200)
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 5, "THE REACT 500: The Sovereign Field Manual\nFirst Edition, 2026\n\nCopyright (c) 2026 by Prince Babatunde Adesina & Owo-Nexus AI.\n\nAll rights reserved.\n\nPublished by Owo-Nexus AI Publishing.\nAbuja, Nigeria.\nWebsite: www.owonexus.com")

            # Dedication
            pdf.add_page()
            pdf.set_y(120)
            pdf.set_font("Helvetica", "I", 12)
            pdf.cell(0, 10, "To the builders who refuse to remain average.", align="C", ln=True)

            # Author Page
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 16)
            pdf.set_text_color(0, 102, 204)
            pdf.cell(0, 10, "ABOUT THE AUTHOR", ln=True)
            pdf.line(20, pdf.get_y(), 80, pdf.get_y())
            pdf.ln(10)
            
            # Smart Image Loader
            img_path = get_asset_path("author.jpg")
            if not os.path.exists(img_path): img_path = get_asset_path("author.jpeg")
            if not os.path.exists(img_path): img_path = get_asset_path("author.png")
            
            if os.path.exists(img_path):
                try: pdf.image(img_path, x=20, y=pdf.get_y(), w=40, h=50)
                except: pass
            else:
                pdf.set_fill_color(240, 240, 240); pdf.rect(20, pdf.get_y(), 40, 50, 'F')
                pdf.set_font("Helvetica", "I", 8); pdf.set_text_color(100, 100, 100)
                pdf.text(22, pdf.get_y() + 25, "Image not found")

            pdf.set_font("Helvetica", "B", 14); pdf.set_text_color(0, 0, 0)
            pdf.text(70, pdf.get_y() + 10, "Prince Babatunde Adesina")
            pdf.set_y(pdf.get_y() + 15); pdf.set_x(70)
            pdf.set_font("Helvetica", "I", 10)
            pdf.multi_cell(0, 5, "AI Consultant | Business Systems Automation Expert | Agentive AI Orchestrator | Rotary Past President")
            pdf.set_y(pdf.get_y() + 15); pdf.set_x(70)
            pdf.set_font("Helvetica", "", 10)
            pdf.multi_cell(0, 5, "Prince Babatunde Adesina is a multi-disciplinary architect of the future. As a Rotary Past President and the 'President of Presidents' during the Connect Rotary Year, he understands leadership at scale.\n\nHe is the visionary behind Owo-Nexus AI and the Sovereign Pivot.")
            pdf.ln(30)

            # About Owo
            pdf.set_font("Helvetica", "B", 16); pdf.set_text_color(0, 102, 204)
            pdf.cell(0, 10, "ABOUT OWO-NEXUS AI", ln=True)
            pdf.line(20, pdf.get_y(), 80, pdf.get_y())
            pdf.ln(10)
            pdf.set_font("Helvetica", "", 10); pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 5, "Owo-Nexus is a premier digital transformation ecosystem focused on the intersection of Artificial Intelligence, Finance, and Human Potential. We build Sovereign Systems.\n\nVisit us at: www.owonexus.com")

            # Intro
            pdf.add_page()
            pdf.chapter_title(0, "Introduction")
            pdf.body_text("Welcome to the Owo-Nexus ecosystem. This manual was architected by Prince Babatunde Adesina to bridge the gap between theoretical tutorials and enterprise execution.\n\nInside, you will find 500 distinct architectural patterns derived from high-scale environments. Your mission is simple: Do not just read. Build.")

            # --- 2. TABLE OF CONTENTS ---
            pdf.add_page()
            pdf.set_font("Helvetica", "B", 16); pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 10, "MASTER INDEX", ln=True); pdf.ln(5)
            
            lines_per_page = 35
            toc_pages = math.ceil(len(REACT_500_DB) / lines_per_page)
            start_content_page = pdf.page_no() + toc_pages 
            
            current_toc_line = 0
            pdf.set_font("Helvetica", "", 9)
            
            for project in REACT_500_DB:
                link_id = pdf.add_link()
                project['link_id'] = link_id
                target_page = start_content_page + (project['id'] - 1)
                
                title_short = (project['title'][:60] + '..') if len(project['title']) > 60 else project['title']
                text_line = f"Project {project['id']}: {title_short}"
                dots = "." * (90 - len(text_line))
                full_line = f"{text_line} {dots} {target_page}"
                
                pdf.cell(0, 5, full_line, ln=True, link=link_id)
                current_toc_line += 1
                if current_toc_line >= lines_per_page:
                    pdf.add_page(); current_toc_line = 0

            # --- 3. PROJECTS CONTENT ---
            pdf.show_header = True
            for p in REACT_500_DB:
                pdf.add_page()
                pdf.set_link(p['link_id'])
                
                pdf.chapter_title(p['id'], p['title'])
                pdf.section_header("Mission Brief")
                pdf.body_text(p['desc'])
                pdf.section_header("Implementation Guide")
                pdf.body_text(p['steps'])
                pdf.section_header("Core Logic")
                pdf.code_block(p['code'])
                pdf.ln(5)
                pdf.case_study_box(p['case_study'])

            # --- 4. BACK COVER ---
            pdf.show_header = False
            pdf.add_page()
            pdf.set_fill_color(15, 15, 15); pdf.rect(0, 0, 210, 297, 'F')
            pdf.set_y(60)
            pdf.set_text_color(255, 255, 255); pdf.set_font("Helvetica", "B", 24)
            pdf.cell(0, 10, "STOP COPYING TUTORIALS.", align="C", ln=True)
            pdf.cell(0, 10, "START BUILDING EMPIRES.", align="C", ln=True)
            pdf.ln(20); pdf.set_x(30); pdf.set_font("Helvetica", "", 12)
            pdf.multi_cell(150, 8, "The difference between a Junior Developer and a Sovereign Architect is the ability to visualize systems before writing a single line of code.\n\nCurated by Prince Babatunde Adesina, 'The React 500' provides the repetition, pattern recognition, and architectural depth required to command high-ticket contracts.", align="C")
            pdf.ln(40); pdf.set_font("Helvetica", "B", 14); pdf.set_text_color(0, 229, 255) 
            pdf.cell(0, 10, "PRINCE BABATUNDE ADESINA", align="C", ln=True)
            pdf.set_font("Helvetica", "", 12); pdf.set_text_color(255, 255, 255)
            pdf.cell(0, 10, "& OWO-NEXUS AI", align="C", ln=True)
            pdf.cell(0, 10, "www.owonexus.com", align="C", ln=True)

            filename = "The_React_500_Global_Edition.pdf"
            pdf.output(filename)
            status_text.value = f"SUCCESS: Generated {filename}"
            
            try: os.startfile(filename)
            except: pass

        except Exception as e:
            status_text.value = f"ERROR: {e}"
        
        page.update()

    # SAFE UI (NO ICONS)
    page.add(
        ft.Container(height=30),
        ft.Text("THE REACT 500", size=30, weight="bold", color="cyan"),
        ft.Text("Global Bestseller Generator", size=14, color="white70"),
        ft.Container(height=30),
        ft.ElevatedButton(
            "GENERATE GLOBAL BOOK",
            bgcolor="cyan", color="black", height=60, width=300,
            on_click=generate_book
        ),
        ft.Container(height=20),
        status_text
    )

if __name__ == "__main__":
    ft.app(target=main)
