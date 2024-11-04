import '@/app/ui/global.css'
import { inter } from '@/app/ui/fonts';

/*
Notes:
* This is the root layout component.
* This component will be rendered on all pages.
* This component is used to set the font and body style.
*/

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${inter.className} antialiased`}>{children}</body>
    </html>
  );
}
