import RevenueChart from "../../ui/dashboard/revenue-chart";
import LatestInvoices from "../../ui/dashboard/latest-invoices";
import { lusitana } from "../../ui/fonts";
import { fetchLatestInvoices } from "../../lib/data";
import { Suspense } from "react";
import {
  RevenueChartSkeleton,
  CardsSkeleton,
  LatestInvoicesSkeleton,
 } from "@/app/ui/skeletons";
import CardWrapper from "@/app/ui/dashboard/cards";

export default async function Page() {
  // the data requests create a request waterfall pattern with the await syntax
  const latestInvoices = await fetchLatestInvoices();

  /* 
  * data right now is statically rendered:
  * meaning the data is rendered on the server during build time
  * - this is good for SEO as content on the page is already available
  * - user often sees cached data, allowing to access quickly
  */

  /*
  * data can be rendered dynamically:
  * meaning the data is rendered on the server for each user at request time (user visits page)
  * - allows real-time data to be displayed (ideal for dashboards)
  * - allows the app the access data generated at request time (eg. cookies, url params)
  * 
  * The disadvantage is, your applications is only as fast as your slowest data fetch
  */

  /*
  * a way to tackle this is streaming data:
  * - this allows clients to access parts of the ui which is ready while other parts are still loading
  * - by streaming you prevent from blocking the whole page from a slow request
  * - in react the components act as streamed chunks of data
  */

  /*
  * in nextjs it is done using the loading.tsx file on the page folder
  * any ui inside loading will be shown until the page is fully loaded
  * 
  * Alternatively, you can use Suspense to unblock other components 
  * while showing a skeleton for the slow component
  */

  return (
    <main>
      <h1 className={`${lusitana.className} mb-4 text-xl md:text-2xl`}>
        Dashboard
      </h1>
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <Suspense fallback={<CardsSkeleton />}>
          <CardWrapper />
        </Suspense>
      </div>
      <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-4 lg:grid-cols-8">
        <Suspense fallback={<RevenueChartSkeleton />}>
          <RevenueChart />
        </Suspense>
        <Suspense fallback={<LatestInvoicesSkeleton />}>
          <LatestInvoices />
        </Suspense>
      </div>
    </main>
  );
}