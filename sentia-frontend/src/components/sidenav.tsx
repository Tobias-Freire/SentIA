'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

const routes = [
  { name: 'Dashboard', path: '/admin/dashboard' },
  { name: 'Feedbacks', path: '/user/feedbacks' },
];

export default function SideNav() {
  const pathname = usePathname();

  return (
    <nav className="flex flex-col gap-4 p-6 bg-white dark:bg-[#18181b] h-full border-r border-gray-200 dark:border-zinc-800 shadow-sm">
      <div className="mb-8">
        <span className="text-2xl font-bold text-gray-800 dark:text-gray-100 tracking-tight">
          Navigation
        </span>
      </div>
      <ul className="flex flex-col gap-2">
        {routes.map((route) => {
          const active = pathname === route.path;
          return (
            <li key={route.path}>
              <Link
                href={route.path}
                className={`flex items-center gap-3 px-4 py-2 rounded-lg transition-colors font-medium
                  ${
                    active
                      ? 'bg-gray-100 dark:bg-zinc-900 text-blue-600 dark:text-blue-400 shadow'
                      : 'text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-zinc-800'
                  }
                `}
              >
                {route.name}
              </Link>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}