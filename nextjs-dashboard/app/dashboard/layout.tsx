import SideNav from "../ui/dashboard/sidenav";

/*
Notes:
* Next js uses file-system based routing.
* To create a route, create a folder with a page.tsx file.
* The content of the page.tsx component will be rendered when the route is accessed.
* A Layout component is something that is shared between all the child components of a page.
* A Layout component can be used to render navbar or footer.
* Advantage of this is partial rendering. Meaning only the component will update and not the navbar or footer.
*/

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen flex-col md:flex-row md:overflow-hidden">
      <div className="w-full flex-none md:w-64" >
        <SideNav />
      </div>
      <div className="flex-grow p-6 md:overflow-y-auto md:p-12">{children}</div>
    </div>
  );
}