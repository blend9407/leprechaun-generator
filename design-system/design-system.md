# Leprechaun Name Generator - Design System

## Color Palette (Irish/Leprechaun Theme)

### Primary Colors
- **Emerald Green**: #2E8B57 (Main brand color)
- **Gold**: #FFD700 (Accent color)
- **Dark Green**: #006400 (Secondary color)
- **Clover Green**: #228B22 (Highlight color)

### Secondary Colors
- **Pot O' Gold Yellow**: #F0E68C (Light accent)
- **Irish Sky Blue**: #87CEEB (Background/UI elements)
- **Shamrock Green**: #009E60 (Success/CTA)
- **Rainbow Gradient**: For special elements

### Neutral Colors
- **Charcoal**: #36454F (Text)
- **Stone Gray**: #808080 (Secondary text)
- **Cloud White**: #FFFFFF (Background)
- **Parchment**: #F5F5DC (Paper/PDF background)

## Typography

### Font Families
- **Headings**: 'Luckiest Guy', cursive (fun, playful)
- **Body**: 'Open Sans', sans-serif (readable, clean)
- **Accent**: 'Irish Grover', cursive (for Irish flair)

### Font Sizes (Mobile-first)
- **H1**: 2.5rem (40px)
- **H2**: 2rem (32px)
- **H3**: 1.5rem (24px)
- **Body**: 1rem (16px)
- **Small**: 0.875rem (14px)

### Font Weights
- **Regular**: 400
- **Medium**: 500
- **Bold**: 700
- **Extra Bold**: 800 (for headings)

## Spacing System (8px base unit)
- **xs**: 4px (0.25rem)
- **sm**: 8px (0.5rem)
- **md**: 16px (1rem)
- **lg**: 24px (1.5rem)
- **xl**: 32px (2rem)
- **xxl**: 48px (3rem)

## Components

### Buttons
```css
.btn-primary {
  background: linear-gradient(135deg, #2E8B57, #006400);
  color: white;
  border: 2px solid #FFD700;
  border-radius: 25px;
  padding: 12px 24px;
  font-weight: 700;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.btn-secondary {
  background: #FFD700;
  color: #006400;
  border: 2px solid #2E8B57;
  border-radius: 25px;
  padding: 12px 24px;
  font-weight: 700;
}
```

### Cards
- **Border radius**: 12px
- **Shadow**: 0 4px 12px rgba(46, 139, 87, 0.15)
- **Background**: White with subtle green gradient
- **Border**: 1px solid #E8F5E9

### Input Fields
- **Border**: 2px solid #C8E6C9
- **Focus border**: 2px solid #2E8B57
- **Border radius**: 8px
- **Padding**: 12px 16px

## Icons & Imagery
- **Leprechaun hat icon** for generator
- **Shamrock** for success/confirmation
- **Pot of gold** for premium features
- **Rainbow** for transitions/loading
- **Celtic knots** for borders/decoration

## Animation & Transitions
- **Hover effects**: Scale up 1.05, shadow elevation
- **Loading**: Rainbow color cycling
- **Success**: Gold sparkle animation
- **Page transitions**: Smooth fade (300ms)

## Responsive Breakpoints
- **Mobile**: 0-767px
- **Tablet**: 768-1023px
- **Desktop**: 1024px+

## Accessibility
- **Contrast ratio**: Minimum 4.5:1 for text
- **Focus states**: Clear gold outline
- **Alt text**: For all images
- **ARIA labels**: For interactive elements
