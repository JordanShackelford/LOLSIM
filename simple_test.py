#!/usr/bin/env python3
"""
Simple Test - Minimal overlay
"""

import tkinter as tk
import execjs

def main():
    print("Starting Simple Test...")
    
    # Create basic window
    root = tk.Tk()
    root.title("Enemy Test")
    root.geometry("400x300")
    
    # Add a label
    label = tk.Label(root, text="Enemy Detection Test\n\nRed boxes should appear here\n\nThis is working!", 
                     font=('Arial', 14), fg='red', bg='black')
    label.pack(expand=True)
    
    print("Window should appear!")
    print("If you can see this window, the overlay system works.")
    
    # Start GUI
    root.mainloop()

def test_js_for_loop_bug():
    # This JS code will throw ReferenceError if not using curly braces
    js_bug = '''
    var caitlyns = [{}, {}];
    try {
        for (const c of caitlyns) c._zedEHitThisCast = false; c._zedERefunded = false;
        return 'NO_ERROR';
    } catch (e) {
        return e.toString();
    }
    '''
    ctx = execjs.compile('function run() {' + js_bug + '}')
    result = ctx.call('run')
    assert 'ReferenceError' in result

def test_js_for_loop_fix():
    # This JS code should NOT throw ReferenceError if using curly braces
    js_fixed = '''
    var caitlyns = [{}, {}];
    try {
        for (const c of caitlyns) { c._zedEHitThisCast = false; c._zedERefunded = false; }
        return 'NO_ERROR';
    } catch (e) {
        return e.toString();
    }
    '''
    ctx = execjs.compile('function run() {' + js_fixed + '}')
    result = ctx.call('run')
    assert result == 'NO_ERROR'

if __name__ == "__main__":
    main() 