import { useEffect, useState } from "react";
import useDateType from "../types/hookTypes/useDateType";

/**
 * 
 * @param interval (ms)
 * @returns date, time, wish
 */
export default function useDate(interval: number): useDateType {
    const locale = "cs"
    const [today, setDate] = useState(new Date())

    useEffect(() => {
        const timer = setInterval(() => {
            setDate(new Date())
        }, interval);
        return () => {
            clearInterval(timer)
        }
    }, [interval])

    const day = today.toLocaleDateString(locale, { weekday: "long" })
    const date = `${day}, ${today.getDate()} ${today.toLocaleDateString(locale, { month: 'long' })}\n\n`;
    const hour = today.getHours()

    var wish = "Dobrý den"
    if (hour < 9) {
        wish = "Dobré ráno"
    }
    else if (hour >= 9 && hour <= 12) {
        wish = "Dobré dopoledne"
    }
    else if (hour === 12) {
        wish = "Dobré poledne"
    }
    else if (hour > 12 && hour <= 18) {
        wish = "Dobré odpoledne"
    }
    else {
        wish = "Dobrý večer"
    }
    const time = today.toLocaleDateString(locale, { hour: "numeric", hour12: false, minute: "numeric" })

    return {
        date,
        time,
        wish
    }
}