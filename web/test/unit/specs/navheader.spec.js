import Navheader from '~/components/navheader.vue'
import Index from '~/pages/index.vue'
import About from '~/pages/about.vue'
import Visualization from '~/pages/visualization.vue'

import { mount } from 'avoriaz'

describe('navheader.vue', () => {
  it('Document page is active', () => {
    const wrapper = mount(Navheader, {
      propsData: { activeSidebar:'doc' }
    })
    expect(wrapper.find('#navheader-doc')[0].hasClass('active')).to.equal(true)
    expect(wrapper.find('#navheader-viz')[0].hasClass('active')).to.equal(false)
    expect(wrapper.find('#navheader-about')[0].hasClass('active')).to.equal(false)
  })

  it('Vizualization page is active', () => {
    const wrapper = mount(Navheader, {
      propsData: { activeSidebar:'viz' }
    })
    expect(wrapper.find('#navheader-doc')[0].hasClass('active')).to.equal(false)
    expect(wrapper.find('#navheader-viz')[0].hasClass('active')).to.equal(true)
    expect(wrapper.find('#navheader-about')[0].hasClass('active')).to.equal(false)
  })

  it('About page is active', () => {
    const wrapper = mount(Navheader, {
      propsData: { activeSidebar:'about' }
    })
    expect(wrapper.find('#navheader-doc')[0].hasClass('active')).to.equal(false)
    expect(wrapper.find('#navheader-viz')[0].hasClass('active')).to.equal(false)
    expect(wrapper.find('#navheader-about')[0].hasClass('active')).to.equal(true)
  })
})