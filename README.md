# Leprechaun Name Generator - UI/UX Design Phase

## Project Overview
A leprechaun name generator with PDF download capabilities, identified as top choice by market research (811% trending growth, extremely easy difficulty, high AI-friendliness).

## Day 1 Deliverables Completed ✅

### 1. Design System Documentation
**Location**: `/design-system/design-system.md`
- Complete Irish/leprechaun aesthetic with green/gold color scheme
- Typography hierarchy (Luckiest Guy, Irish Grover, Open Sans)
- Spacing system (8px base unit)
- Component styles and states
- Responsive breakpoints

### 2. Main Generator Page Mockup
**Location**: `/mockups/generator-mockup.html`
- Mobile-first responsive design
- Name generator interface with input/output
- PDF template preview gallery
- Premium upgrade section
- User dashboard layout
- Fully functional HTML/CSS with interactive elements

### 3. PDF Template Designs (2 completed)
**Location**: `/pdf-templates/`

#### Template 1: Classic Emerald Certificate
- **File**: `classic-emerald-template.html`
- **Style**: Elegant Celtic design with emerald green/gold palette
- **Features**: Celtic knot borders, parchment background, shamrock motifs
- **Size**: A4 portrait (210mm × 297mm)

#### Template 2: Rainbow Magic Certificate
- **File**: `rainbow-magic-template.html`
- **Style**: Vibrant rainbow gradient with glitter effects
- **Features**: Animated sparkles, rainbow arch, gold glitter border
- **Size**: A4 landscape (297mm × 210mm)

#### Template Specifications
- **File**: `template-specifications.md`
- Detailed design specifications for both templates
- Implementation notes for PDF generation
- Color profiles (RGB for web, CMYK for print)
- Asset requirements list

## Development Coordination

### Next Steps for Developer

#### Phase 1: Core Generator (Day 2)
1. **Backend Setup**
   - Create Flask/FastAPI server
   - Implement name generation algorithm
   - Database for user names/sessions

2. **PDF Generation**
   - Integrate HTML-to-PDF library (jsPDF/WeasyPrint)
   - Template rendering system
   - Download functionality

3. **Frontend Integration**
   - Convert mockup to React/Vue components
   - API integration for name generation
   - PDF preview system

#### Phase 2: Premium Features (Day 3)
1. **User Authentication**
   - Signup/login system
   - Dashboard for saved names

2. **Premium Templates**
   - Additional template designs
   - Customization options

3. **Payment Integration**
   - Stripe/PayPal setup
   - Subscription management

### Technical Requirements
- **Token Budget**: $5 AI tokens total
- **Timeframe**: 5-day challenge (3 days setup)
- **Location**: Work in this directory
- **Images**: Use Pexels API for Irish-themed images

### Assets Needed
Check `/assets/images/` for existing Irish-themed images
If none available, use Pexels API with key: `KkThisbhnzOOj7p2sRyxKgIcgYkUHRVBLGxWL6y2BZBldpbVy73PzFJd`

## Design System Usage

### Colors
```css
--emerald: #2E8B57;
--dark-green: #006400;
--gold: #FFD700;
--parchment: #F5F5DC;
--charcoal: #36454F;
```

### Typography
- **Headings**: 'Luckiest Guy', cursive
- **Names**: 'Irish Grover', cursive
- **Body**: 'Open Sans', sans-serif

### Components
Reusable components in `/components/` folder (to be created)

## File Structure
```
leprechaun-generator/
├── pdf-templates/          # PDF template designs
├── mockups/               # Page mockups
├── design-system/         # Design specifications
├── components/            # Reusable UI components
├── assets/               # Images, fonts, styles
│   ├── images/
│   └── css/
└── README.md             # This file
```

## Coordination Notes
- **Token Conservation**: Reuse components to minimize AI token usage
- **Responsive Priority**: Mobile-first approach
- **PDF Quality**: Ensure print-ready templates
- **Theme Consistency**: Maintain Irish/leprechaun aesthetic

## Success Metrics
- **Day 1**: Design system + 2 templates ✅
- **Day 2**: Functional generator + 1 template PDF
- **Day 3**: Premium features + user dashboard
- **Day 4-5**: Marketing + revenue generation

---
*Last updated: January 13, 2026*
*UI/UX Designer - Agent Zero System*
