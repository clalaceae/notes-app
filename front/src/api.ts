// api.ts

export async function fetchHelper<T>(
  url: string,
  init: RequestInit = {},
): Promise<T> {
  const res = await fetch(url, init)

  if (!res.ok) {
    throw new Error(`Request failed: ${res.status}`)
  }

  if (res.status === 204) {
    return undefined as T
  }

  return res.json() as Promise<T>
}